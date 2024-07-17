from enum import Enum
from typing import List, Optional, Tuple
import mysql.connector

import context


class DatabaseType(Enum):
    """
    Encodes the type of database that is being used.
    """

    MARIADB = "mariadb"
    MYSQL = "mysql"
    TIDB = "tidb"

    @staticmethod
    def from_str(value: str) -> "DatabaseType":
        if value == "mariadb":
            return DatabaseType.MARIADB
        elif value == "mysql":
            return DatabaseType.MYSQL
        elif value == "tidb":
            return DatabaseType.TIDB
        else:
            raise ValueError(f"Unsupported database type: {value}")

    def used_port(self):
        """
        Returns the default port used by the database type.
        """
        if self == DatabaseType.TIDB:
            return 4000
        else:
            return 3306


class DatabaseTypeAndVersion:
    """
    Encodes the database type and version
    """

    def __init__(self, database_type: DatabaseType, version: str):
        """
        Creates a new DatabaseTypeAndVersion object.

        :param database_type: The type of the database.
        :param version: The version of the database.
        """
        self.database_type = database_type
        self.version = version

    def __str__(self):
        return f"{self.database_type.value}-{self.version}"

    def __eq__(self, other: "DatabaseTypeAndVersion"):
        if other is None:
            return False
        return (
            self.database_type == other.database_type and self.version == other.version
        )

    def __hash__(self) -> int:
        return hash((self.database_type, self.version))

    def to_docker_hub_images_and_tags(self) -> List[Tuple[str, str]]:
        """
        Returns a list of possible docker hub images and tags for the database.
        The order is given by preference (i.e. the first element is the most preferred).

        This is used because we sometimes want to use custom self-built images.

        e.g. [([[registry name]]/dbms, mariadb-10.5.8), (library/mariadb, 10.5.8)]
        """
        custom_registry = context.Context.get_context().docker_hub_registry
        custom_image = (
            f"{custom_registry}/dbms",
            f"{self.database_type.value}-{self.version}",
        )
        official_image = None

        if self.database_type == DatabaseType.MARIADB:
            official_image = ("library/mariadb", self.version)
        elif self.database_type == DatabaseType.MYSQL:
            official_image = ("library/mysql", self.version)
        elif self.database_type == DatabaseType.TIDB:
            official_image = ("pingcap/tidb", self.version)
        else:
            raise ValueError(f"Unsupported database type: {self.database_type}")

        return [custom_image, official_image]


class DatabaseConnection:
    """
    Encodes the database connection details
    """

    def __init__(
        self,
        database_type_and_version: DatabaseTypeAndVersion,
        host: Optional[str] = None,
        port: Optional[int] = None,
        user: Optional[str] = None,
    ):
        self.database_type_and_version = database_type_and_version
        self.host = host
        self.port = port
        self.user = user

    def to_connection(self, autocommit=None) -> mysql.connector.MySQLConnection:
        """
        Returns a MySQL connection object.
        """
        args = dict()
        if self.host:
            args["host"] = self.host
        if self.user:
            args["user"] = self.user
        if self.port:
            args["port"] = self.port
        if autocommit is not None:
            args["autocommit"] = autocommit

        conn = mysql.connector.connect(**args)
        return conn
