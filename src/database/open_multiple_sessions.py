import logging, subprocess

from .config import DatabaseTypeAndVersion, DatabaseType
from .provide_database_server import DatabaseProvider
import context

def open_multiple_sessions(db: DatabaseTypeAndVersion, nr_instances: int):
    """
    Opens multiple terminal windows, each with a database session.
    """
    logging.info(f"Opening {nr_instances} database sessions for {db}.")
    with DatabaseProvider(db) as provider:
        connection = provider.database_connection
        
        processes = []
        for i in range(nr_instances):
            match db.database_type:
                case DatabaseType.MYSQL:
                    # open a terminal window with a mysql session
                    command = context.Context.get_context().open_terminal_command +\
                            f" -- {connection.db_binaries_folder}/mysql -h {connection.host}" +\
                            f" -P {connection.port} -u {connection.user}  --password='{connection.password}'"
                    logging.info(f"Running command: {command}")
                    proc = subprocess.Popen(
                        [command],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        shell=True
                    )
                    processes.append(proc)
                case DatabaseType.MARIADB:
                    # open a terminal window with a mysql session
                    command = context.Context.get_context().open_terminal_command +\
                            f" -- {connection.db_binaries_folder}/mysql"
                    logging.info(f"Running command: {command}")
                    proc = subprocess.Popen(
                        [command],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        shell=True
                    )
                    processes.append(proc)
                case DatabaseType.TIDB:
                    # open a terminal window with a tidb session
                    command = context.Context.get_context().open_terminal_command +\
                            f" -- mysql --comments --host 127.0.0.1 --port 4000 -u root"
                    logging.info(f"Running command: {command}")
                    proc = subprocess.Popen(
                        [command],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        shell=True
                    )
                    processes.append(proc)
                case _:
                    raise ValueError(f"Unsupported database type: {db.database_type}")
        
        logging.info("Waiting for the database sessions to be closed...")
        print("Waiting for the database sessions to be closed...", end='', flush=True)
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