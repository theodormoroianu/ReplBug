"""
This module contains the functions that are used to build the docker images.

Optionally, the images can be pushed or pulled from a registry.
"""

import os, logging, pathlib

import context
import database.helpers as helpers


def build_image(dockerfile: pathlib.Path, push_to_registry: bool):
    """
    Builds a specific docker image.

    :param dockerfile: The path to the dockerfile. It should follow the naming conventions.

    E.g. The file `mariadb-10.10.1.Dockerfile` will build an image with the name `[[registry name]]/mariadb-10.10.1`.
    """

    print(f"Trying to build the image from the dockerfile: {dockerfile}")
    logging.info(f"Trying to build the image from the dockerfile: {dockerfile}")

    assert dockerfile.exists(), f"File {dockerfile} does not exist."
    assert not dockerfile.is_dir(), f"File {dockerfile} is a directory."
    assert dockerfile.name.endswith(
        ".Dockerfile"
    ), f"File {dockerfile} is not a Dockerfile."

    # The folder containing the dockerfile.
    folder = dockerfile.parent
    name = dockerfile.name[: -len(".Dockerfile")]

    # The name of the image, including the registry.
    image_name = f"{context.Context.get_context().docker_hub_registry}/dbms:{name}"

    # Build the docker image.
    command = f"podman build --tag {image_name} --file {dockerfile} {folder}"
    helpers.run_command(command)

    if push_to_registry:
        command = f"podman push {image_name}"
        retcode = helpers.run_command(command)
        if retcode != 0:
            print(f"Failed to push the image: {image_name}")
            logging.error(f"Failed to push the image: {image_name}")


def build_all_images(push_to_registry: bool):
    """
    Builds all of the images found in the dockerfiles directory.
    """
    # Get all files in the dockerfiles directory.
    dockerfiles_folder = context.Context.get_context().dockerfiles_dir
    docker_files = os.listdir(dockerfiles_folder)
    docker_files = [f for f in docker_files if f.endswith(".Dockerfile")]

    print(f"Building the following images: {docker_files}")
    logging.info(f"Building the following images: {docker_files}")

    # Build all the images.
    for docker_file in docker_files:
        build_image(dockerfiles_folder / docker_file, push_to_registry)
