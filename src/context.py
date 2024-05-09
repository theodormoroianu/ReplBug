"""
This module provides the necessary context for the application.
"""

import pathlib
import os
from dotenv import load_dotenv

if not load_dotenv():
    print(f"WARNING: Could not load the `.env` file. Make sure to have one in the root of the project.")

class Context:
    """
    Provides the necessary context for the application.
    """
    context = None

    def __init__(self):
        self.cache_folder: pathlib.Path = pathlib.Path(os.getenv("CACHE_FOLDER_PATH"))
        assert self.cache_folder is not None, "The `CACHE_FOLDER_PATH` environment variable is not set."
        if not self.cache_folder.exists():
            self.cache_folder.mkdir(parents=True)
        self.stop_database_server_at_startup = (os.getenv("STOP_DATABASE_SERVER_AT_STARTUP").lower() == "true")

        match os.getenv("LOGGING_LEVEL"):
            case "DEBUG":
                self.logging_level = "DEBUG"
            case "INFO":
                self.logging_level = "INFO"
            case "WARNING":
                self.logging_level = "WARNING"
            case _:
                self.logging_level = "INFO"

    @staticmethod
    def get_context():
        """
        Returns the context of the application.
        """
        if Context.context is None:
            Context.context = Context()
        return Context.context