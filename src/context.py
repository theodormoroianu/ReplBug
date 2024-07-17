"""
This module provides the necessary context for the application.
"""

import pathlib, os
from dotenv import load_dotenv

if not load_dotenv():
    print(
        "WARNING: Could not load the `.env` file. Make sure to have one in the root of the project."
    )


class Context:
    """
    Provides the necessary context for the application.
    """

    instance = None

    def __init__(self):
        # The root of the project.
        self.project_root = pathlib.Path(__file__).parent.parent

        # Folder where stuff like logs is stored.
        self.cache_folder: pathlib.Path = self.project_root / ".cache"
        if not self.cache_folder.exists():
            self.cache_folder.mkdir()

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
        if self.open_terminal_command is None:
            print(
                "WARNING: The `TERMINAL_WINDOW_COMMAND` is not set in the `.env` file."
            )

        # Read the data path
        self.data_folder_path = self.project_root / "data"

        # The location of the "dockerfiles" directory.
        self.dockerfiles_dir = self.project_root / "dockerfiles"

        # Check if we should push images to a remote registry when built.
        self.docker_push_on_build = os.getenv("DOCKER_PUSH_ON_BUILD") == "true"

        # Remote registry to push / pull images from.
        self.docker_hub_registry = os.getenv("DOCKER_HUB_REGISTRY")

    @staticmethod
    def get_context():
        """
        Returns the context of the application.
        """
        if Context.instance is None:
            Context.instance = Context()
        return Context.instance
