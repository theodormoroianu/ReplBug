import interactor.database_interactor as database_interactor
from database.config import DatabaseTypeAndVersion, DatabaseType
import database.provide_database_server as provide_database_server
import mysql.connector
import time

def my_fn(_):
    db = DatabaseTypeAndVersion(DatabaseType.MYSQL, version="8.0.34")

    with provide_database_server.DatabaseProvider(db) as provider:
        connection = provider.database_connection

        # connect to the database
        conn = mysql.connector.connect(
            host=connection.host,
            user=connection.user,
            password=connection.password
        )

        # create a cursor
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE test_db")
        cursor.execute("USE test_db")

        cursor.execute("CREATE TABLE test_table (id INT PRIMARY KEY, name VARCHAR(255))")
        cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'test')")
        cursor.execute("SELECT * FROM test_table")
        print(cursor.fetchall())

_commands = {
    "database": ("interact with the database", database_interactor.database_interactor),
    "my_fn": ("my_fn", my_fn)
}

def interactor():
    """
    Provides a command line interface for the BugHunter tool.
    """
    while True:
        command = input("> ")
        command = command.lower().split()
        if command == []:
            continue

        if command[0] == "exit":
            break
        elif command[0] == "help":
            print("Available commands:")
            for command, (description, _) in _commands.items():
                print(f"  {command}: {description}")
        elif command[0] in _commands:
            try:
                _commands[command[0]][1](command[1:])
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"Unknown command: {command[0]}")
            print("Type 'help' to see the available commands.")
