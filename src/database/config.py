from enum import Enum

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
            port: int,
            user: str,
            password: str,
            database: str):
        self.database_type_and_version = database_type_and_version
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database