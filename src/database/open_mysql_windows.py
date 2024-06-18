import logging, subprocess

from .config import DatabaseTypeAndVersion, DatabaseType, DatabaseConnection
from .provide_db_container import DatabaseProvider
import context


def mysql_cli_command(conn: DatabaseConnection):
    """
    Returns the command to open a mysql session.
    """
    assert conn.host != None
    assert conn.port != None
    assert conn.user != None

    return f"mysql -h {conn.host} -P {conn.port} -u {conn.user}"


def open_multiple_sessions(db: DatabaseTypeAndVersion, nr_instances: int):
    """
    Opens multiple terminal windows, each with a database session.
    """
    logging.info(f"Opening {nr_instances} database sessions for {db}.")
    with DatabaseProvider(db) as db_provider:
        processes = []
        for i in range(nr_instances):

            # open a terminal window with a mysql session
            command = (
                context.Context.get_context().open_terminal_command
                + " -- "
                + mysql_cli_command(db_provider.db_connection)
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
        print("Waiting for the database sessions to be closed...", end="", flush=True)
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
        print(" DONE")
