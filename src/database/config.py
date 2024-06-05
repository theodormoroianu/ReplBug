from enum import Enum
from typing import Optional, Tuple
import pathlib
import mysql.connector


class DatabaseType(Enum):
    """
    Encodes the type of database that is being used.
    """

    MARIADB = "mariadb"
    MYSQL = "mysql"
    TIDB = "tidb"
    MARIADB_DEBUG = "mariadb-debug"

    @staticmethod
    def from_str(value: str) -> "DatabaseType":
        if value == "mariadb":
            return DatabaseType.MARIADB
        elif value == "mysql":
            return DatabaseType.MYSQL
        elif value == "tidb":
            return DatabaseType.TIDB
        elif value == "mariadb-debug":
            return DatabaseType.MARIADB_DEBUG
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

    def to_docker_image_and_tag(self) -> Tuple[str, str]:
        """
        returns the docker image and tag for the database.
        e.g. (docker.io/library/mariadb, 10.5.8)
        """
        if self.database_type == DatabaseType.MARIADB:
            return ("docker.io/library/mariadb", self.version)
        elif self.database_type == DatabaseType.MYSQL:
            return ("docker.io/library/mysql", self.version)
        elif self.database_type == DatabaseType.TIDB:
            # https://hub.docker.com/r/pingcap/tidb/tags
            return ("docker.io/pingcap/tidb", f"v{self.version}")
        elif self.database_type == DatabaseType.MARIADB_DEBUG:
            return ("mariadb-debug", self.version)
        else:
            raise ValueError(f"Unsupported database type: {self.database_type}")

    def needs_to_be_pulled(self) -> bool:
        """
        Returns whether the database image needs to be pulled.
        """
        return self.database_type != DatabaseType.MARIADB_DEBUG


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
        password: Optional[str] = None,
        socket: Optional[str] = None,
    ):
        self.database_type_and_version = database_type_and_version
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.socket = socket

    def to_connection(self, autocommit=None) -> mysql.connector.MySQLConnection:
        """
        Returns a MySQL connection object.
        """
        args = dict()
        if self.socket:
            args["unix_socket"] = self.socket
        if self.host:
            args["host"] = self.host
        if self.user:
            args["user"] = self.user
        if self.password:
            args["password"] = self.password
        if self.port:
            args["port"] = self.port
        if autocommit is not None:
            args["autocommit"] = autocommit

        conn = mysql.connector.connect(**args)
        return conn
