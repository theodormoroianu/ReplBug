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
        # Read cache folder location.
        self.cache_folder: pathlib.Path = pathlib.Path(os.getenv("CACHE_FOLDER_PATH"))
        assert self.cache_folder is not None, "The `CACHE_FOLDER_PATH` environment variable is not set."
        if not self.cache_folder.exists():
            self.cache_folder.mkdir(parents=True)

        # Read the database server stop flag.
        self.stop_database_server_at_startup = (os.getenv("STOP_DATABASE_SERVER_AT_STARTUP").lower() == "true")

        # Read the logging level.
        match os.getenv("LOGGING_LEVEL"):
            case "DEBUG":
                self.logging_level = "DEBUG"
            case "INFO":
                self.logging_level = "INFO"
            case "WARNING":
                self.logging_level = "WARNING"
            case _:
                self.logging_level = "INFO"

        # Read the path to the terminal console.
        self.open_terminal_command = os.getenv("TERMINAL_WINDOW_COMMAND")

        # Read the data path
        self.data_folder_path = pathlib.Path(os.getenv("DATA_FOLDER_PATH"))

        # Read the path to dockerfiles
        self.dockerfiles_path = pathlib.Path(os.getenv("DOCKERFILES_FOLDER_PATH"))

    @staticmethod
    def get_context():
        """
        Returns the context of the application.
        """
        if Context.context is None:
            Context.context = Context()
        return Context.context