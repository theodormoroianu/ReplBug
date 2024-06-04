"""
This module is responsible for providing the necessary binaries for the database.
"""

import os
from typing import Optional, Tuple
import pathlib
import subprocess
import mysql.connector
import time
import logging
import signal
import atexit

from .config import DatabaseTypeAndVersion, DatabaseType, DatabaseConnection
import context
from .download_and_extract import download_and_extract_db_binaries


def _run_database_server(
    root_folder: Optional[pathlib.Path],
    db: DatabaseTypeAndVersion,
    reconfigure_db: bool,
) -> Tuple[DatabaseConnection, subprocess.Popen]:
    """
    Runs the database server.
    """

    db_connection: Optional[DatabaseConnection] = None
    server_process: Optional[subprocess.Popen] = None

    if db.database_type == DatabaseType.TIDB:
        # start the tidb server
        # tiup handles the download and installation of the binaries
        logging.info("Starting the TiDB server...")
        server_process = subprocess.Popen(
            [f"tiup"] + f"playground v{db.version} --db 1 --pd 3 --kv 3".split(),
            stdin=subprocess.DEVNULL,
        )
        db_connection = DatabaseConnection(
            database_type_and_version=db,
            host="127.0.0.1",
            port=4000,
            user="root",
        )
    else:  # We have MySQL or MariaDB
        # Delete the old data folder if required
        data_folder = root_folder / "data"
        if reconfigure_db and data_folder.exists():
            os.system(f"rm -rf {data_folder}")
        if not data_folder.exists():
            reconfigure_db = True

        if reconfigure_db:
            logging.info("Configuring the database server...")
            if db.database_type == DatabaseType.MYSQL:
                os.system(
                    f"cd {root_folder} && ./bin/mysqld --initialize-insecure 2> /dev/null > /dev/null"
                )
            else:
                os.system(
                    f"cd {root_folder} && ./scripts/mysql_install_db --datadir={data_folder} 2> /dev/null > /dev/null"
                )
            logging.info("Database server configured.")

        logging.info(f"Starting the database server at {root_folder}")
        if db.database_type == DatabaseType.MYSQL:
            server_process = subprocess.Popen(
                [f"{root_folder}/bin/mysqld", "--user=root"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            db_connection = DatabaseConnection(
                database_type_and_version=db, socket="/tmp/mysql.sock", user="root"
            )
        else:
            server_process = subprocess.Popen(
                [f"{root_folder}/bin/mysqld", f"--datadir={data_folder}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            db_connection = DatabaseConnection(
                database_type_and_version=db,
                socket="/tmp/mysql.sock",
            )

    # Wait for database to be reachable.
    before = time.time()
    while True:
        try:
            conn = db_connection.to_connection()
            conn.ping()
            break
        except Exception as e:
            if time.time() - before > 30:
                logging.error("Database failed to start.")
                print("Database failed to start.")
                print(f"Database and type: {db}")
                print(f"PID of the server process: {server_process.pid}")
                input("Press enter to continue...")
                _stop_database_server(root_folder, db, server_process)
                raise e
            time.sleep(0.8)
            logging.info("Waiting for the database to start...")
    logging.info("Database started.")
    return db_connection, server_process


def _stop_database_server(
    root_folder: pathlib.Path,
    db: DatabaseTypeAndVersion,
    server_process: subprocess.Popen,
) -> int:
    """
    Stops the database server.
    """
    if db.database_type == DatabaseType.TIDB:
        logging.info(f"Stopping the TiDB server at {root_folder}")
        server_process.terminate()
        return server_process.wait()

    if db.database_type == DatabaseType.MYSQL:
        logging.info(f"Stopping the MySQL server at {root_folder}")
        # stop the mysql server
        os.system(f"{root_folder}/bin/mysqladmin -u root shutdown")
        retcode = server_process.wait()
        # delete the data folder
        # os.system(f"rm -rf {root_folder}/data")
        return retcode

    elif db.database_type == DatabaseType.MARIADB:
        logging.info(f"Stopping the MariaDB server at {root_folder}")
        # stop the mariadb server
        os.system(f"{root_folder}/bin/mariadb-admin shutdown")
        retcode = server_process.wait()
        # delete the data folder
        # os.system(f"rm -rf {root_folder}/data")
        return retcode

    else:
        raise ValueError(f"Unsupported database type: {db.database_type}")


class DatabaseProvider:
    """
    Provides and cleans the necessary binaries for a specific database.
    """

    _running_server_process: Optional[subprocess.Popen] = None
    _running_server_path: Optional[pathlib.Path] = None
    _running_server_type_and_version: Optional[DatabaseTypeAndVersion] = None
    _running_server_connection: Optional[DatabaseConnection] = None
    _running_server_busy = False

    @staticmethod
    def _stop_running_server():
        if DatabaseProvider._running_server_process:
            logging.info("Stopping the running database server.")
            _stop_database_server(
                DatabaseProvider._running_server_path,
                DatabaseProvider._running_server_type_and_version,
                DatabaseProvider._running_server_process,
            )
            DatabaseProvider._running_server_process = None
            DatabaseProvider._running_server_path = None
            DatabaseProvider._running_server_type_and_version = None
            DatabaseProvider._running_server_connection = None

    @staticmethod
    def _start_running_server(db: DatabaseTypeAndVersion, reconfigure_db: bool):
        assert DatabaseProvider._running_server_process is None
        DatabaseProvider._running_server_path = download_and_extract_db_binaries(db)
        db_connection, server_process = _run_database_server(
            DatabaseProvider._running_server_path, db, reconfigure_db=reconfigure_db
        )
        DatabaseProvider._running_server_type_and_version = db
        DatabaseProvider._running_server_process = server_process
        DatabaseProvider._running_server_connection = db_connection

    def __init__(
        self, database_type_and_version: DatabaseTypeAndVersion, reconfigure_db=False
    ):
        self.database_type_and_version = database_type_and_version
        self.reconfigure_db = reconfigure_db
        self.database_connection = None

    def __enter__(self):
        """
        Starts the database and populates the `database_connection` attribute.
        """
        assert (
            not self.__class__._running_server_busy
        ), "Another database server is already running."
        self.__class__._running_server_busy = True

        if (
            self.database_type_and_version
            == self.__class__._running_server_type_and_version
            and not self.reconfigure_db
        ):
            logging.info(
                f"Reusing the running database server for {self.database_type_and_version}."
            )
            self.database_connection = self.__class__._running_server_connection
            return self

        logging.info(
            f"Starting the database server for {self.database_type_and_version}."
        )
        self.__class__._stop_running_server()
        self.__class__._start_running_server(
            self.database_type_and_version, self.reconfigure_db
        )

        self.database_connection = self.__class__._running_server_connection
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        assert self.__class__._running_server_busy, "No database server is running."
        self.__class__._running_server_busy = False

    @staticmethod
    def _kill_running_server_script_exiting():
        # print("Killing the running database server...", end="", flush=True)
        DatabaseProvider._stop_running_server()
        # print("done.")


# register the cleanup function
atexit.register(DatabaseProvider._kill_running_server_script_exiting)
