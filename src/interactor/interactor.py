import cmd, readline, logging, pathlib

import database.open_mysql_windows as db_open_sessions
import database.provide_db_container as db_provider
import interactor.helpers as helpers
import testcase.run_bugs as run_bugs
import testcase.bug_list as bug_list
import context
import database.build as db_build

HISTORY_FILE = context.Context.get_context().cache_folder / "cmd_history"


class MainInteractor(cmd.Cmd):
    prompt = "> "
    instance = None

    @staticmethod
    def get_instance():
        if MainInteractor.instance is None:
            MainInteractor.instance = MainInteractor()
        return MainInteractor.instance

    def __init__(self):
        super().__init__()

    def preloop(self):
        # Load commmand history
        try:
            readline.read_history_file(HISTORY_FILE)
        except Exception:
            pass

    def postloop(self):
        # Dump commmand history
        try:
            import readline

            readline.set_history_length(100)
            readline.write_history_file(HISTORY_FILE)
        except Exception:
            pass

    
    def do_build(self, arg: str):
        """
        Builds the custom docker files required for testing some of the bugs.
        """
        if arg == "help" or arg == "--help":
            self.help_build()
            return
        push = False
        arg = arg.split()
        if arg[-1] == "push":
            arg = arg[:-1]
            push = True
        if arg:
            try:
                for dockerfile in arg:
                    db_build.build_image(pathlib.Path(dockerfile), push)
            except Exception as e:
                print("Error: ", e)
                logging.error(e)
        else:
            try:
                db_build.build_all_images(push_to_registry=push)
            except Exception as e:
                print("Error: ", e)
                logging.error(e)

    def help_build(self):
        print("Builds the custom docker images required for testing some of the bugs.")
        print("If a dockerfile is provided, it should follow naming conventions.")
        print("If 'push' is provided, the image will be pushed to the registry.\n")
        print("Usage:   build [dockerfile] [push]")
        print("Example: build dockerfiles/tidb-v4.0.0.tikb.Dockerfile push")


    def do_shell(self, arg: str):
        """
        Spawns multiple shells connected to a database server.
        """
        try:
            nr_shells = int(arg.split()[0])
            arg = " ".join(arg.split()[1:])
            db_and_version = helpers.parse_db_type_and_version(arg)
        except Exception:
            self.help_shell()
            return
        db_open_sessions.open_multiple_sessions(db_and_version, nr_instances=nr_shells)

    def help_shell(self):
        print("Spawns multiple shells connected to a database server.")
        print("Usage:    shell <NR SHELLS> <DB TYPE> <VERSION>")
        print("Example:  shell 4 mysql 8.0.34")


    def do_server(self, arg: str):
        """
        Starts a database server and waits for the user to connect to it.
        """
        try:
            db_and_version = helpers.parse_db_type_and_version(arg)
        except Exception:
            self.help_server()
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
            print("Stopping the database server...  ", end="", flush=True)
        print("DONE")

    def help_server(self):
        print("Starts a database server and waits for the user to connect to it.")
        print("Usage:    server <DB TYPE> <VERSION>")
        print("Example:  server mysql 8.0.34")


    def do_test(self, arg: str):
        """Runs the bugs."""
        run_bugs.run_bugs(arg.split() or [".*"])

    def help_test(self):
        print("Runs the bugs.")
        print("If a regex is provided, only the bugs that match the regex will be run.")
        print("Usage:    test [<REGEX>]")
        print("Example:  test TIDB.* ")


    def do_list(self, arg: str):
        """Lists the available bugs."""
        regexes = arg.split() or [".*"]
        bugs = bug_list.get_bugs(regexes)
        if not bugs:
            print("No bugs found for the provided patterns.")
            return

        print("Available bugs:")
        for bug in bugs:
            print(f" * {bug}")

    def help_list(self):
        print("Lists the available bugs.")
        print("If a regex is provided, only the bugs that match the regex will be listed.")
        print("Usage:    list [<REGEX>]")
        print("Example:  list TIDB.* ")


    def do_help(self, _arg):
        """Shows help menu."""
        print("Available commands:")
        print("  shell    : Spawns multiple shells connected to a database server.")
        print("  server   : Starts a database server and waits for the user to connect to it.")
        print("  build    : Builds the custom docker files required for testing some of the bugs.")
        print("  test     : Tests specific bugs, by running them against a specificed database server.")
        print("  list     : Lists the available bugs.")
        print("  help     : Shows this help menu.")
        print("  exit     : Exit the tool.")

    def help_help(self):
        print("Shows help menu.")


    def precmd(self, line: str) -> str:
        """
        Correctly handle exit and EOF.
        """
        if line == "EOF":
            return "quit"
        return super().precmd(line)

    def default(self, line: str):
        args = line.split()

        if len(args) > 0 and args[0] in ["q", "quit", "exit"]:
            return True
        
        return super().default(line)

    def process_external_arg(self, args: str):
        """
        Processes the external arguments.
        If the arguments are empty, it starts the command loop.
        """
        if args != "":
            self.onecmd(args)
        else:
            self.cmdloop()
