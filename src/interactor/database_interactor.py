import database.config as db_config
import database.provide_database_server as db_provider

def _download_database(command: list[str]):
    """
    Downloads a database.
    """
    if len(command) != 2:
        print("Usage: download <DB TYPE> <VERSION>")
        return

    database_type = command[0]
    database_type = db_config.DatabaseType.from_str(database_type.lower())

    version = command[1]

    db_and_version = db_config.DatabaseTypeAndVersion(database_type, version)

    provider = db_provider.DatabaseProvider(db_and_version)
    provider._download_and_extract_binaries()


_database_interactor_commands = {
    "download": ("<DB TYPE> <VERSION>  download a database", _download_database),
}

def database_interactor(command: list[str]):
    """
    Allows the user to download and interact with a database.
    """
    if command == [] or command[0] == "help":
        print("Available commands:")
        for command, (description, _) in _database_interactor_commands.items():
            print(f"  {command}: {description}")
        return
    elif command[0] in _database_interactor_commands:
        _database_interactor_commands[command[0]][1](command[1:])
    else:
        print(f"Unknown command: {command[0]}")
        print("Type 'help' to see the available commands.")
