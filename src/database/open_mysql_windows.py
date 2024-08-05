import logging, subprocess
from typing import List

from .config import DatabaseTypeAndVersion, DatabaseConnection
from .provide_db_container import DatabaseProvider
import context


def mysql_cli_command(conn: DatabaseConnection, db_name: str):
    """
    Returns the command to open a mysql session.
    """
    assert conn.host != None
    assert conn.port != None
    assert conn.user != None

    return f"mysql -h {conn.host} -P {conn.port} -u {conn.user} -D {db_name} --ssl-mode=DISABLED"


def open_multiple_sessions(db: DatabaseTypeAndVersion, nr_instances: int):
    """
    Opens multiple terminal windows, each with a database session.
    """
    logging.info(f"Opening {nr_instances} database sessions for {db}.")
    print("Starting the database server... ", end="", flush=True)
    with DatabaseProvider(db) as db_provider:
        print("                DONE")
        conn = db_provider.db_connection.to_connection()
        conn.cursor().execute("drop database if exists testdb;")
        conn.cursor().execute("create database testdb;")

        processes: List[subprocess.Popen] = []
        for _ in range(nr_instances):

            # open a terminal window with a mysql session
            command = (
                context.Context.get_context().open_terminal_command
                + " -- "
                + mysql_cli_command(db_provider.db_connection, "testdb")
            )

            logging.info(f"Running command: {command}")
            proc = subprocess.Popen(
                [command],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                shell=True,
            )
            processes.append(proc)

        logging.info("Waiting for the database sessions to be closed...")
        print("Waiting for windows to be closed (or CTRL+C)... ", end="", flush=True)
        try:
            # wait for the processes to finish
            for proc in processes:
                proc.wait()
                proc.kill()
        except KeyboardInterrupt:
            # kill all the processes
            for proc in processes:
                proc.kill()
        logging.info("All database sessions have been closed.")
        print("DONE")
        print("Stopping the database server... ", end="", flush=True)
    print("                DONE")
