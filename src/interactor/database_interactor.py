import logging
import cmd
import time

import database.config as db_config
import database.provide_database_server as db_provider
import database.download_and_extract as db_download
import database.open_multiple_sessions as db_open_sessions
import context
import interactor.helpers as helpers


class DatabaseInteractor(cmd.Cmd):
    prompt = "db> "
    instance = None

    @staticmethod
    def get_instance():
        if DatabaseInteractor.instance is None:
            DatabaseInteractor.instance = DatabaseInteractor()
        return DatabaseInteractor.instance

    def __init__(self):
        super().__init__()

    def do_list(self, arg):
        """Lists the downloaded available databases."""
        cache_path = context.Context.get_context().cache_folder / "databases"
        if not cache_path.exists():
            print("No databases downloaded.")
            return

        print("Available databases:")
        for db in sorted(cache_path.iterdir()):
            print(f" * {db.name}")

    def help_list(self):
        print("Lists the downloaded available databases.")

    def do_download(self, arg: str):
        """Downloads a database."""
        try:
            db, version = arg.replace("-", " ").split()
            db = db_config.DatabaseType.from_str(db)
        except Exception as e:
            self.help_download()
            return

        logging.info(f"Downloading database {db} version {version}, requested by user.")
        db_and_version = db_config.DatabaseTypeAndVersion(db, version)
        db_download.download_and_extract_db_binaries(db_and_version)
        logging.info(f"Done.")
        print("Downloaded database.")

    def help_download(self):
        print("Downloads a database.")
        print("Usage: download <DB TYPE> <VERSION>")
        print("Example: download mysql 8.0.34")

    def do_spawn(self, arg: str):
        """
        Spawns multiple shells connected to a database server.
        """
        try:
            nr_shells, db, version = arg.replace("-", " ").split()
            db = db_config.DatabaseType.from_str(db)
        except Exception as e:
            self.help_spawn()
            return
        db_open_sessions.open_multiple_sessions(
            db_config.DatabaseTypeAndVersion(db, version), int(nr_shells)
        )

    def do_start_server(self, arg: str):
        """
        Starts a database server and waits for the user to connect to it.
        """
        try:
            db_and_version = helpers.parse_db_type_and_version(arg)
        except Exception as e:
            self.help_start_server()
            return

        with db_provider.DatabaseProvider(db_and_version) as provider:
            connection = provider.database_connection
            if db_and_version.database_type != db_config.DatabaseType.TIDB:
                print(f"Host:          {connection.host}")
                print(f"Port:          {connection.port}")
                print(f"User:          {connection.user}")
                print(f"Password:      {connection.password}")
                print(
                    f"Connect with:  {db_open_sessions.mysql_cli_command(db_and_version)}"
                )
            else:
                time.sleep(2)

            print("\nDatabase server started. Press Enter to stop.", flush=True)
            try:
                input()
            except KeyboardInterrupt:
                pass

    def help_start_server(self):
        print("Starts a database server and waits for the user to connect to it.")
        print("Usage: start_server <DB TYPE>-<VERSION>")
        print("Example: start_server mysql-8.0.34")

    def help_spawn(self):
        print("Spawns multiple shells connected to a database server.")
        print("Usage: spawn <NR SHELLS> <DB TYPE> <VERSION>")
        print("Example: spawn 4 mysql 8.0.34")

    def do_help(self, arg):
        """Shows help menu."""
        print("Available commands:")
        print("  list         : Lists the downloaded available databases.")
        print("  download     : Downloads a database.")
        print("  spawn        : Spawns multiple shells connected to a database server.")
        print(
            "  start_db     : Starts a database server and waits for the user to connect to it."
        )

    def help_help(self):
        print("Shows help menu.")

    def process_external_arg(self, args: str):
        """
        Processes the external arguments.
        If the arguments are empty, it starts the command loop.
        """
        if args != "":
            self.onecmd(args)
        else:
            self.cmdloop()

    def precmd(self, line: str) -> str:
        if line == "EOF":
            print("")
            return "quit"
        return super().precmd(line)

    def default(self, line: str) -> None:
        args = line.split()
        if len(args) > 0 and args[0] in ["q", "quit", "exit"]:
            return True
        return super().default(line)
