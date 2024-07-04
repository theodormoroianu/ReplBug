"""
This module is responsible for providing the necessary binaries for the database.
"""

from .config import DatabaseTypeAndVersion
from .podman_connection import PodmanConnection


class DatabaseProvider:
    """
    Provides and cleans the necessary binaries for a specific database.
    """

    def __init__(
        self,
        database_type_and_version: DatabaseTypeAndVersion,
        kill_server_after_testcase: bool = False,
    ):
        """
        Creates a new database provider.

        :param database_type_and_version: The database type and version to provide.
        :param kill_server_after_testcase: If the server should be stopped after running the test.
        """
        self.container_id = None
        self.db_connection = None
        self.db_type_and_version = database_type_and_version
        self.kill_server_after_testcase = kill_server_after_testcase

    def __enter__(self):
        """
        Starts the database and populates the `database_connection` attribute.
        """
        podman_connection = PodmanConnection.get_instance()
        self.container_id, self.db_connection = podman_connection.create_container(
            self.db_type_and_version
        )

        return self

    def get_logs(self):
        """
        Get the logs of the container.
        """
        podman_connection = PodmanConnection.get_instance()
        return podman_connection.get_logs(self.container_id)

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stops the database.
        """
        podman_connection = PodmanConnection.get_instance()
        podman_connection.stop_container(
            self.container_id, not self.kill_server_after_testcase
        )
        self.container_id = None
        self.db_connection = None
