"""
This module contains custom exceptions for the application.
"""


class DatabaseVersionNotFoundError(Exception):
    """
    Raised when the database version is not found.
    """

    def __init__(self, database_type: str, version: str):
        super().__init__(f"Database version {version} not found for {database_type}")
        self.database_type = database_type
        self.version = version
