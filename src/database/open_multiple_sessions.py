import logging, subprocess

from .config import DatabaseTypeAndVersion, DatabaseType
from .provide_database_server import DatabaseProvider
import context

def mysql_cli_command(db: DatabaseTypeAndVersion):
    """
    Returns the command to open a mysql session.
    """
    if db.database_type == DatabaseType.MARIADB:
        return "mysql -S /tmp/mysql.sock"
    elif db.database_type == DatabaseType.MYSQL:
        return "mysql -S /tmp/mysql.sock -u root"
    elif db.database_type == DatabaseType.TIDB:
        return "mysql --comments --host 127.0.0.1 --port 4000 -u root"
    else:
        raise ValueError(f"Unsupported database type: {db.database_type}")


def open_multiple_sessions(db: DatabaseTypeAndVersion, nr_instances: int):
    """
    Opens multiple terminal windows, each with a database session.
    """
    logging.info(f"Opening {nr_instances} database sessions for {db}.")
    with DatabaseProvider(db):        
        processes = []
        for i in range(nr_instances):
            
            # open a terminal window with a mysql session
            command = context.Context.get_context().open_terminal_command +\
                        " -- " +\
                        mysql_cli_command(db)

            logging.info(f"Running command: {command}")
            proc = subprocess.Popen(
                [command],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                shell=True
            )
            processes.append(proc)
        
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