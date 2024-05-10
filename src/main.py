#! /usr/bin/env python3
import argparse, os, logging, datetime

import context
import interactor.interactor as interactor

def main():    
    parser = argparse.ArgumentParser(description="Run the BugHunter tool.")

    # stop the database server
    if context.Context.get_context().stop_database_server_at_startup:
        os.system("pgrep mysqld | xargs kill 2> /dev/null")
        os.system("pgrep mariadbd | xargs kill 2> /dev/null")

    # start logging
    logging_folder = context.Context.get_context().cache_folder / "logs"
    logging_folder.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=logging_folder / datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log"),
        format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d:%H:%M:%S",
        level=context.Context.get_context().logging_level
    )

    # run the interactor
    logging.info("Starting the BugHunter tool.")
    try:
        interactor.MainInteractor.get_instance().cmdloop()
    except KeyboardInterrupt as e:
        print("")
    logging.info("Exiting the BugHunter tool.")

if __name__ == '__main__':
    main()