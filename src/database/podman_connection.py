import subprocess, logging, time, atexit, os
import podman.client as client
from typing import Dict, List, Tuple
from collections import defaultdict
from podman.domain.containers import Container

from .config import DatabaseTypeAndVersion, DatabaseConnection
from . import helpers


class PodmanConnection:
    """
    Starts and stops the podman server, and provides the necessary context for the application.
    """

    _instance = None

    @staticmethod
    def free_resources():
        """
        Stops the podman server.
        """
        if PodmanConnection._instance is not None:
            del PodmanConnection._instance
            PodmanConnection._instance = None

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of the PodmanConnection.
        """
        if PodmanConnection._instance is None:
            PodmanConnection._instance = PodmanConnection()
        return PodmanConnection._instance

    def __init__(self):
        """
        This:
            1. Starts the podman service.
            2. Initializes the podman client.
        """
        # Start the server.
        logging.info("Starting the podman daemon...")
        self.podman_server_proc = subprocess.Popen(
            ["podman", "system", "service", "--time=0"]
        )

        # Start the client. It might take a few seconds for the server
        # to become reachable.
        logging.info("Connecting to the podman daemon...")
        self.podman_client = client.PodmanClient()
        time_before = time.time()
        while time.time() - time_before < 5:
            try:
                if not self.podman_client.ping():
                    raise ConnectionError()
                break
            except Exception:
                time.sleep(0.1)
                logging.info("Waiting for the podman daemon to start...")
        else:
            logging.error("Connection to the podman daemon failed.")
            print("Error connecting to the podman daemon.")
            print("Please make sure that podman is installed.")
            raise ConnectionError("Error connecting to the podman daemon.")

        # Mapping from containerID to container object
        self.containers: Dict[
            str, Tuple[Container, DatabaseTypeAndVersion, DatabaseConnection]
        ] = {}

        # Containers that are running but not currently used.
        # We check that the db is reachable before using it, to avoid
        # providing a crashed DB to the user.
        self.unused_containers: Dict[
            DatabaseTypeAndVersion, List[Tuple[Container, DatabaseConnection]]
        ] = defaultdict(list)

        # Map storing for each container the number of log lines to ignore (mostly the ones generated
        # by the database server starting up)
        self.log_characters_to_ignore: Dict[str, int] = defaultdict(int)

    def create_container(
        self, db_and_version: DatabaseTypeAndVersion
    ) -> Tuple[str, DatabaseConnection]:
        """
        Creates a container for the given database type and version.
        returns the container id and the database connection.
        """
        logging.debug(f"new container for {db_and_version} requested.")
        # Maybe we have a container that is not currently used.
        if self.unused_containers[db_and_version]:
            logging.info(f"Re-using a container for {db_and_version}.")
            container, db_connection = self.unused_containers[db_and_version].pop()
            self.containers[container.id] = (container, db_and_version, db_connection)
            return container.id, db_connection

        # The container image we need.
        image_name, tag = db_and_version.to_docker_image_and_tag()

        # Pull the image if necessary.
        if db_and_version.needs_to_be_pulled:
            logging.info(f"Pulling the database server for {db_and_version}.")
            self.podman_client.images.pull(repository=image_name, tag=tag)
            logging.info(f"Image {image_name}:{tag} pulled.")

        # Create the container
        host_port = helpers.get_free_port()
        container_port = db_and_version.database_type.used_port()

        # Environment variables for the container
        environment = {
            "MYSQL_ALLOW_EMPTY_PASSWORD": "yes",
            "MARIADB_ALLOW_EMPTY_ROOT_PASSWORD": "yes",
        }

        try:
            container = self.podman_client.containers.create(
                image=f"{image_name}:{tag}",
                ports={f"{container_port}/tcp": host_port},
                environment=environment,
                auto_remove=False,
                network_mode="bridge",
            )
        except Exception as e:
            logging.info(
                "Unable to create the container. Maybe the image is not built?"
            )
            # Log the error and raise a new one
            logging.error(e)
            print(
                f"Unable to create the container. Image {image_name}:{tag} is not present."
            )
            raise e

        container.start()
        logging.info(f"Container {container.id} started on port {host_port}")

        db_connection = DatabaseConnection(
            db_and_version, host="127.0.0.1", port=host_port, user="root"
        )

        self.containers[container.id] = (container, db_and_version, db_connection)

        # make sure that the DB is reachable
        time_before = time.time()
        logging.info("Waiting for the database server to start...")
        while time.time() - time_before < 30:
            try:
                db_connection.to_connection().ping()
                break
            except Exception as e:
                time.sleep(0.1)
        else:
            logging.error("Connection to the database server failed.")
            print("Error connecting to the database server.")
            print("Please make sure that the database server is running:")
            print(
                f"Command: docker run -p {host_port}:{container_port} {image_name}:{tag}"
            )
            input("Press Enter to continue...")
            raise ConnectionError("Error connecting to the database server.")
        logging.info("Database server started.")

        # Mark the log lines to ignore
        self.log_characters_to_ignore[container.id] = len(self.get_logs(container.id))

        return container.id, db_connection

    def get_logs(self, container_id: str) -> str:
        """
        Get the logs of the container. If some lines are marked to
        be skipped (see `log_lines_to_ignore`), they are skipped.
        """
        container, _, _ = self.containers[container_id]
        logs = container.logs(stdout=True, stderr=True)
        logs_dump = (
            logs.decode() if isinstance(type(logs), bytes) else b"".join(logs).decode()
        )
        return logs_dump[self.log_characters_to_ignore[container_id] :]

    def stop_container(self, container_id: str, try_reuse: bool = True):
        """
        Stops the container with the given id.
        If `try_reuse` is True, the container is tested to check if it can be re-used.

        :param container_id: The id of the container to stop.
        :param try_reuse: If the container should be tested for re-use.
        """
        container, db_and_version, db_connection = self.containers[container_id]
        logging.debug(
            f"Stopping container {container_id} of type {db_and_version} (try-reuse = {try_reuse})..."
        )
        try:
            # If we can't reuse it, throw an exception.
            if not try_reuse:
                raise ValueError("Container can't be re-used (imposed by testcase).")

            # Try to re-use container
            # Make a few SQL queries to check if the DB is still alive
            conn = db_connection.to_connection()
            conn.ping()
            cursor = conn.cursor()
            cursor.execute("drop database if exists testdb;")
            cursor.execute("create database testdb;")
            cursor.execute("create table testdb.testtable (a int);")
            cursor.execute("insert into testdb.testtable values (1);")
            cursor.execute("drop table testdb.testtable;")

            self.unused_containers[db_and_version].append((container, db_connection))
            self.log_characters_to_ignore[container_id] += len(
                self.get_logs(container_id)
            )
            logging.debug(f"Recycling container {container_id}.")
            del self.containers[container_id]
        except Exception as e:
            logging.debug(f"Error re-using container {container_id}: {e}")
            # Can't re-use container. Try to stop it.
            try:
                container.stop(timeout=0)
                container.remove(v=True)
            except Exception as e:
                container.remove(v=True)
            del self.containers[container_id]
            del self.log_characters_to_ignore[container_id]

    # run when the object is deleted
    def __del__(self):
        """
        Stops the podman server.
        """
        logging.info("Cleaning containers...")
        containers_ids = []
        for _, (container, _, _) in self.containers.items():
            containers_ids.append(container.id)
        for _, l in self.unused_containers.items():
            for container, _ in l:
                containers_ids.append(container.id)
        for container_id in containers_ids:
            os.system(f"podman kill {container_id} > /dev/null")
            os.system(f"podman rm {container_id} > /dev/null")

        self.podman_server_proc.kill()


atexit.register(PodmanConnection.free_resources)
