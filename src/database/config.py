from enum import Enum
from typing import Optional
import pathlib
import mysql.connector

class DatabaseType(Enum):
    """
    Encodes the type of database that is being used.
    """
    MARIADB = 'mariadb'
    MYSQL = 'mysql'
    TIDB = 'tidb'

    @staticmethod
    def from_str(value: str) -> 'DatabaseType':
        if value == 'mariadb':
            return DatabaseType.MARIADB
        elif value == 'mysql':
            return DatabaseType.MYSQL
        elif value == 'tidb':
            return DatabaseType.TIDB
        else:
            raise ValueError(f"Unsupported database type: {value}")


class DatabaseTypeAndVersion:
    """
    Encodes the database type and version
    """
    def __init__(self, database_type: DatabaseType, version: str):
        self.database_type = database_type
        self.version = version

    def __str__(self):
        return f"{self.database_type.value}-{self.version}"
    
    
class DatabaseConnection:
    """
    Encodes the database connection details
    """
    def __init__(
            self,
            database_type_and_version: DatabaseTypeAndVersion,
            host: str,
            port: Optional[int] = None,
            user: Optional[str] = None,
            password: Optional[str] = None):
        self.database_type_and_version = database_type_and_version
        self.host = host
        self.port = port
        self.user = user
        self.password = password
    
    def to_connection(self) -> mysql.connector.MySQLConnection:
        """
        Returns a MySQL connection object.
        """
        args = {
            'host': self.host
        }
        if self.user:
            args['user'] = self.user
        if self.password:
            args['password'] = self.password
        if self.port:
            args['port'] = self.port

        conn = mysql.connector.connect(**args)
        return conn