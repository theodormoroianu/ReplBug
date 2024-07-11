#! /usr/bin/env python3
import argparse, os, logging, datetime, sys

import context
import interactor.interactor as interactor


def main():
    # Before doing any work, make sure that `podman` is installed.
    if os.system("command -v podman > /dev/null") != 0:
        print("Please install `podman` before running the tool.")
        sys.exit(1)

    # start logging
    logging_folder = context.Context.get_context().cache_folder / "logs"
    logging_folder.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=logging_folder
        / datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log"),
        format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
        level=context.Context.get_context().logging_level,
    )

    # run the interactor
    logging.info("Starting the BugHunter tool.")
    try:
        interactor.MainInteractor.get_instance().process_external_arg(
            " ".join(sys.argv[1:])
        )
    except KeyboardInterrupt:
        print("")
    logging.info("Exiting the BugHunter tool.")


if __name__ == "__main__":
    main()
