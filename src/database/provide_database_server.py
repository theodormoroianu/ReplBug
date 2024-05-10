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

from .config import DatabaseTypeAndVersion, DatabaseType, DatabaseConnection
import context
from .download_and_extract import download_and_extract_db_binaries

def _run_database_server(root_folder: pathlib.Path, db: DatabaseTypeAndVersion) -> Tuple[DatabaseConnection, subprocess.Popen]:
    """
    Runs the database server.
    """
    # delete existing data if any
    data_folder = root_folder / "data"
    if data_folder.exists():
        os.system(f"rm -rf {data_folder}")
    
    if db.database_type == DatabaseType.MYSQL:
        # start the mysql server
        logging.info(f"Starting the MySQL server at {root_folder}")
        os.system(f"cd {root_folder} && ./bin/mysqld --initialize-insecure --user=root 2> /dev/null > /dev/null")
        
        # start the mysql server in a separate process, ignore the output
        server_process = subprocess.Popen([f"{root_folder}/bin/mysqld", "--user=root"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return [
            DatabaseConnection(
                database_type_and_version=db,
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="",
                db_binaries_folder=root_folder/"bin"
            ),
            server_process
        ]
    elif db.database_type == DatabaseType.MARIADB:
        # start the mariadb server
        logging.info(f"Starting the MariaDB server at {root_folder}")  
        os.system(f"cd {root_folder} && ./scripts/mysql_install_db --datadir={data_folder} 2> /dev/null > /dev/null")

        # start the mariadb server in a separate process, ignore the output
        server_process = subprocess.Popen([f"{root_folder}/bin/mysqld", f"--datadir={data_folder}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return [
            DatabaseConnection(
                database_type_and_version=db,
                host="localhost",
                port=3306,
                user=os.getlogin(),
                password="",
                database="",
                db_binaries_folder=root_folder/"bin"
            ),
            server_process
        ]
    else:
        raise ValueError(f"Unsupported database type: {db.database_type}")

def _stop_database_server(root_folder: pathlib.Path, db: DatabaseTypeAndVersion, server_process: subprocess.Popen) -> int:
    """
    Stops the database server.
    """
    if db.database_type == DatabaseType.MYSQL:
        logging.info(f"Stopping the MySQL server at {root_folder}")
        # stop the mysql server
        os.system(f"{root_folder}/bin/mysqladmin -u root shutdown")
        retcode = server_process.wait()

        # delete the data folder
        os.system(f"rm -rf {root_folder}/data")
        return retcode
    elif db.database_type == DatabaseType.MARIADB:
        logging.info(f"Stopping the MariaDB server at {root_folder}")
        # stop the mariadb server
        os.system(f"{root_folder}/bin/mariadb-admin shutdown")
        retcode = server_process.wait()

        # delete the data folder
        os.system(f"rm -rf {root_folder}/data")
        return retcode
    else:
        raise ValueError(f"Unsupported database type: {db.database_type}")
    


class DatabaseProvider:
    """
    Provides and cleans the necessary binaries for a specific database.
    """
    def __init__(self, database_type_and_version: DatabaseTypeAndVersion):
        self.database_type_and_version = database_type_and_version
        self.database_connection: Optional[DatabaseConnection] = None
        self.server_process: Optional[subprocess.Popen] = None
        self.db_path: Optional[pathlib.Path] = None


    def __enter__(self):
        """
        Starts the database and populates the `database_connection` attribute.
        """
        self.db_path = download_and_extract_db_binaries(self.database_type_and_version)
        print("Configuring the database server...", end='', flush=True)
        self._run_database()
        print(" DONE")

        # wait for the database to start
        match self.database_type_and_version.database_type:
            case DatabaseType.MYSQL:
                logging.info("Waiting for the database to start...")
                print(f"Waiting for the database to start..", end='')
                while True:
                    try:
                        conn = mysql.connector.connect(
                            host=self.database_connection.host,
                            user=self.database_connection.user,
                            password=self.database_connection.password
                        )
                        break
                    except Exception as e:
                        logging.debug("Received error: " + e)
                        print(f".", end='', flush=True)
                        logging.info("Retrying in 1 second...")
                        time.sleep(0.5)
                print(" DONE")
                logging.info("Database started.")
            case DatabaseType.MARIADB:
                logging.info("Waiting for the database to start...")
                print(f"Waiting for the database to start..", end='')
                while True:
                    try:
                        conn = mysql.connector.connect(
                            host=self.database_connection.host,
                        )
                        break
                    except Exception as e:
                        logging.debug("Received error: " + e)
                        print(f".", end='', flush=True)
                        logging.info("Retrying in 1 second...")
                        time.sleep(0.5)
                print(" DONE")
                logging.info("Database started.")
            case _:
                raise ValueError(f"Unsupported database type: {self.database_type_and_version.database_type}")
        
        return self

    def _run_database(self):
        """
        Runs the database with the given type and version.
        """
        db_connection, server_process = _run_database_server(
            self.db_path,
            self.database_type_and_version
        )
        self.database_connection = db_connection
        self.server_process = server_process

    def _stop_database(self):
        """
        Stops the database.
        """
        print("Stopping the database server...", end="", flush=True)
        _stop_database_server(
            self.db_path,
            self.database_type_and_version,
            self.server_process
        )
        print(" DONE")
        self.database_connection = None
        self.server_process = None

    def __exit__(self, exc_type, exc_value, traceback):
        self._stop_database()
        pass
