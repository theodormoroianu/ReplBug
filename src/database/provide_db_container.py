"""
This module is responsible for providing the necessary binaries for the database.
"""

import time
from typing import Optional, Set, Tuple, Dict
import atexit
import logging
import podman.client as client
import podman
import socket
import subprocess
from podman.domain.containers import Container

from .config import DatabaseTypeAndVersion, DatabaseType, DatabaseConnection
from . import helpers
from .podman_connection import PodmanConnection
import context


class DatabaseProvider:
    """
    Provides and cleans the necessary binaries for a specific database.
    """

    def __init__(
        self, database_type_and_version: DatabaseTypeAndVersion, reconfigure_db=False
    ):
        self.container_id = None
        self.db_connection = None
        self.db_type_and_version = database_type_and_version

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
        podman_connection.stop_container(self.container_id)
        self.container_id = None
        self.db_connection = None
