import logging, cmd, os, subprocess

import database.open_mysql_windows as db_open_sessions
import database.provide_db_container as db_provider
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

    def do_build(self, _arg):
        """
        Builds the custom docker files required for testing some of the bugs.
        """
        print("Building the custom docker files... ")
        logging.info("Building the custom docker files... ")
        project_root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        docker_files_path = os.path.join(project_root_path, "dockerfiles")
        subprocess.run(
            ["sh", "build.sh"],
            cwd=docker_files_path,
        )
        print("DONE")


    def do_spawn(self, arg: str):
        """
        Spawns multiple shells connected to a database server.
        """
        try:
            nr_shells = int(arg.split()[0])
            arg = " ".join(arg.split()[1:])
            db_and_version = helpers.parse_db_type_and_version(arg)
        except Exception:
            self.help_spawn()
            return
        db_open_sessions.open_multiple_sessions(db_and_version, nr_instances=nr_shells)

    def do_start(self, arg: str):
        """
        Starts a database server and waits for the user to connect to it.
        """
        try:
            db_and_version = helpers.parse_db_type_and_version(arg)
        except Exception:
            self.help_start()
            return

        print("Starting the database server... ", end="", flush=True)
        with db_provider.DatabaseProvider(db_and_version) as provider:
            print("DONE")
            connection = provider.db_connection
            
            # Create a test database.
            conn = connection.to_connection()
            conn.cursor().execute("drop database if exists testdb;")
            conn.cursor().execute("create database testdb;")

            print(f"Host:          {connection.host}")
            print(f"Port:          {connection.port}")
            print(f"User:          {connection.user}")
            print(f"Connect with:  {db_open_sessions.mysql_cli_command(connection, "testdb")}")
            print("\nPress Enter to stop the database server...")
            try:
                input()
            except KeyboardInterrupt:
                pass
            print("Stopping the database server... ", end="", flush=True)
        print("DONE")

    def help_start(self):
        print("Starts a database server and waits for the user to connect to it.")
        print("Usage: start <DB TYPE>-<VERSION>[-local]")
        print("Example: start_server mysql-8.0.34-local")

    def help_spawn(self):
        print("Spawns multiple shells connected to a database server.")
        print("Usage: spawn <NR SHELLS> <DB TYPE> <VERSION>")
        print("Example: spawn 4 mysql 8.0.34")

    def help_build(self):
        print("Builds the custom docker files required for testing some of the bugs.")
        print("Usage: build")
        print("Example: build")

    def do_help(self, arg):
        """Shows help menu."""
        print("Available commands:")
        print("  spawn    : Spawns multiple shells connected to a database server.")
        print(
            "  start    : Starts a database server and waits for the user to connect to it."
        )
        print(
            "  build    : Builds the custom docker files required for testing some of the bugs."
        )
        print("  help     : Shows this help menu.")
        print("  exit     : Exit to the main menu.")

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

    def default(self, line: str):
        args = line.split()
        if len(args) > 0 and args[0] in ["q", "quit", "exit"]:
            return True
        return super().default(line)
