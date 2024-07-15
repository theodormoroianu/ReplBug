import os, logging, pathlib

import context


def build_image(dockerfile: pathlib.Path):
    """
    Builds a specific docker image.

    :param dockerfile: The path to the dockerfile. It should follow the naming conventions.
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

    # Get the image name and version.
    image_name = name.split("-")[0]
    version = name[len(image_name) + 1 :]

    # Build the docker image.
    os.system(
        f"podman build --tag {image_name}:{version} --file {dockerfile.name} {folder}"
    )


def build_all_images():
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
        build_image(dockerfiles_folder / docker_file)
