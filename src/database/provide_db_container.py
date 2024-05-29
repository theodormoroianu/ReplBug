"""
This module is responsible for providing the necessary binaries for the database.
"""
import time
from typing import Optional, Set, Tuple, Dict
from podman.domain.containers import Container

import atexit
import logging
import podman.client as client
import podman
import socket

from .config import DatabaseTypeAndVersion, DatabaseType, DatabaseConnection
import context

def get_free_port():
    """
    Returns a free port.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]
    

class DatabaseProvider:
    """
    Provides and cleans the necessary binaries for a specific database.
    """
    # active db containers 
    containers: Dict[DatabaseTypeAndVersion, Tuple[Container, DatabaseConnection]] = {}
    
    # the active containers
    busy_containers: Set[DatabaseTypeAndVersion] = set()

    # the podman client
    podman_client: Optional[podman.PodmanClient] = None

    def __init__(self, database_type_and_version: DatabaseTypeAndVersion, reconfigure_db=False):
        self.database_type_and_version = database_type_and_version
        self.reconfigure_db = reconfigure_db
        self.database_connection = None

    def __enter__(self):
        """
        Starts the database and populates the `database_connection` attribute.
        """
        assert self.database_type_and_version not in self.busy_containers, \
                "Another database server is already running."
        
        try:
            if self.podman_client is None:
                logging.info("Connecting to the podman daemon...")
                self.podman_client = client.PodmanClient()
            if not self.podman_client.ping():
                raise Exception("Connection to the podman daemon failed.")
        except Exception as e:
            logging.error(f"Error connecting to the podman daemon: {e}")
            print("Error connecting to the podman daemon.")
            print("Please run `podman system service --time=0`.")
            raise Exception("Error connecting to the podman daemon.")
            
        if self.database_type_and_version not in self.containers and not self.reconfigure_db:
            # need to start new server
            host_port = get_free_port()
            image_name, tag = self.database_type_and_version.to_docker_image_and_tag()
            container_port = 3306
            password = "1234"
            if self.database_type_and_version.database_type == DatabaseType.TIDB:
                container_port = 4000
                password = ""
            
            environment = {
                "MYSQL_ROOT_PASSWORD": password,
                "MARIADB_ROOT_PASSWORD": password,
                "MARIADB_PASSWORD": password
            }
            # download and start the container
            logging.info(f"Starting the database server for {self.database_type_and_version}.")
            print(f"Pulling {image_name}:{tag}...", end='', flush=True)
            self.podman_client.images.pull(repository=image_name, tag=tag)
            print(" done.")
            container = self.podman_client.containers.create(
                image=f"{image_name}:{tag}",
                ports={f"{container_port}/tcp": host_port},
                environment=environment,
                auto_remove=True,
            )
            container.start()
            logging.info(f"Container {container.id} started on port {host_port}")
            
            db_connection = DatabaseConnection(
                self.database_type_and_version,
                host="127.0.0.1",
                port=host_port,
                password=password,
                user="root"
            )

            self.containers[self.database_type_and_version] = (container, db_connection)

        else:
            logging.info(f"Reusing the running database server for {self.database_type_and_version}.")
        
        self.database_connection = self.containers[self.database_type_and_version][1]

        # Make sure the container is reachable
        before = time.time()
        while True:
            try:
                conn = self.database_connection.to_connection()
                conn.ping()
                break
            except Exception as e:
                if time.time() - before > 30:
                    logging.error("Database failed to start.")
                    print("Database failed to start.")
                    print(f"Database and type: {self.database_type_and_version}")
                    print(f"ID: {self.containers[self.database_type_and_version][0].id}")
                    input("Press enter to continue...")
                    raise e
                time.sleep(0.8)
                logging.info("Waiting for the database to start...")

        self.busy_containers.add(self.database_type_and_version)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.busy_containers.remove(self.database_type_and_version)

    @staticmethod
    def kill_all_running_containers():
        assert DatabaseProvider.busy_containers == set(), "Some containers are still running."
        print("Killing all the running containers...", end='', flush=True)
        for container, _ in DatabaseProvider.containers.values():
            container.stop(timeout=0)
            print(".", end='', flush=True)
        print("done.")

# register the cleanup function
atexit.register(DatabaseProvider.kill_all_running_containers)
