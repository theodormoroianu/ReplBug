import interactor.database_interactor as database_interactor
import cmd

class MainInteractor(cmd.Cmd):
    prompt = '> '
    instance = None

    @staticmethod
    def get_instance():
        if MainInteractor.instance is None:
            MainInteractor.instance = MainInteractor()
        return MainInteractor.instance

    def __init__(self):
        super().__init__()

    def do_database(self, arg):
        """Allows the user to download and interact with a database."""
        try:
            database_interactor.DatabaseInteractor\
                .get_instance()\
                .process_external_arg(arg)
        except KeyboardInterrupt as e:
            print("")
            pass

    def do_help(self, arg):
        """Shows help menu."""
        print("Available commands:")
        print("  database  : Allows the user to download and interact with a database.")
        print("  help      : Shows this help menu")
        print("  quit      : Quits the program")

    def help_help(self):
        print("Shows help menu.")
    
    def precmd(self, line: str) -> str:
        if line == "EOF":
            print("")
            return "quit"
        return super().precmd(line)

    def default(self, line: str) -> None:
        args = line.split()

        if len(args) > 0 and args[0] in ["q", "quit", "exit"]:
            return True
        
        if len(args) > 0 and args[0] == "db":
            self.do_database(" ".join(args[1:]))
            return
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
            