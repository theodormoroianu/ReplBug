import subprocess
import logging
import time
from typing import Dict, Tuple
import podman.client as client
from podman.domain.containers import Container

from .config import DatabaseTypeAndVersion, DatabaseConnection
from . import helpers

class PodmanConnection:
    """
    Starts and stops the podman server, and provides the necessary context for the application.
    """

    _instance = None

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
        self.podman_server_proc = subprocess.Popen(["podman", "system", "service", "--time=0"])

        # Start the client. It might take a few seconds for the server
        # to become reachable.
        logging.info("Connecting to the podman daemon...")
        self.podman_client = client.PodmanClient()
        time_before = time.time()
        while time.time() - time_before < 5:
            try:
                if not self.podman_client.ping():
                    raise Exception()
                break
            except Exception as e:
                time.sleep(0.1)
                logging.info("Waiting for the podman daemon to start...")
        else:
            logging.error("Connection to the podman daemon failed.")
            print("Error connecting to the podman daemon.")
            print("Please make sure that podman is installed.")
            raise Exception("Error connecting to the podman daemon.")

        # Mapping from containerID to container object
        self.containers: Dict[str, Tuple[Container, DatabaseTypeAndVersion, DatabaseConnection]] = {}


    def create_container(self, db_and_version: DatabaseTypeAndVersion) -> Tuple[str, DatabaseConnection]:
        """
        Creates a container for the given database type and version.
        returns the container id and the database connection.
        """
        # The container image we need.
        image_name, tag = db_and_version.to_docker_image_and_tag()
        
        # Pull the image if necessary.
        if db_and_version.needs_to_be_pulled():
            logging.info(f"Pulling the database server for {db_and_version}.")
            self.podman_client.images.pull(repository=image_name, tag=tag)
            logging.info(f"Image {image_name}:{tag} pulled.")

        # Create the container
        host_port = helpers.get_free_port()
        image_name, tag = db_and_version.to_docker_image_and_tag()
        container_port = db_and_version.database_type.used_port()
        
        # Environment variables for the container
        environment = {
            "MYSQL_ALLOW_EMPTY_PASSWORD": "yes",
            "MARIADB_ALLOW_EMPTY_ROOT_PASSWORD": "yes",
        }

        container = self.podman_client.containers.create(
            image=f"{image_name}:{tag}",
            ports={f"{container_port}/tcp": host_port},
            environment=environment,
            auto_remove=False,
        )
        container.start()
        logging.info(f"Container {container.id} started on port {host_port}")
        
        db_connection = DatabaseConnection(
            db_and_version,
            host="127.0.0.1",
            port=host_port,
            user="root"
        )

        self.containers[container.id] = (container, db_and_version, db_connection)
        
        # make sure that the DB is reachable
        time_before = time.time()
        while time.time() - time_before < 15:
            try:
                db_connection.to_connection().ping()
                break
            except Exception as e:
                time.sleep(0.1)
                logging.info("Waiting for the database server to start...")
        else:
            logging.error("Connection to the database server failed.")
            print("Error connecting to the database server.")
            print("Please make sure that the database server is running:")
            print(f"Command: docker run -p {host_port}:{container_port} {image_name}:{tag}")
            raise Exception("Error connecting to the database server.")

        return container.id, db_connection
    
    def get_logs(self, container_id: str) -> str:
        """
        Get the logs of the container.
        """
        container, _, _ = self.containers[container_id]
        return container.logs().decode()

    def stop_container(self, container_id: str) -> str:
        """
        Stops the container with the given id.
        """
        container, _, _ = self.containers[container_id]
        container.stop(timeout=0)
        container.remove()
        del self.containers[container_id]

    # run when the object is deleted
    def __del__(self):
        """
        Stops the podman server.
        """
        if self.containers != {}:
            logging.info("Cleaning all containers...")
            # stop and delete all containers
            for container_id, (container, _, _) in self.containers.items():
                container.stop(timeout=0)
                container.remove()
            self.podman_server_proc.kill()