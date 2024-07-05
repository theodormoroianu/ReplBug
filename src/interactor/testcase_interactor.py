import cmd

import testcase.run_bugs as run_bugs
import testcase.bug_list as bug_list


class TestcaseInteractor(cmd.Cmd):
    prompt = "test> "
    instance = None

    @staticmethod
    def get_instance():
        if TestcaseInteractor.instance is None:
            TestcaseInteractor.instance = TestcaseInteractor()
        return TestcaseInteractor.instance

    def __init__(self):
        super().__init__()

    def do_test(self, arg):
        """Runs the "test" function."""
        run_bugs.test()

    def do_run(self, arg: str):
        """Runs the bugs."""
        run_bugs.run_bugs(arg.split() or [".*"])

    def do_bug(self, arg):
        """Runs the bugs."""
        self.do_run(arg)

    def do_help(self, arg):
        """Shows help menu."""
        print("Available commands:")
        print("  test    : Runs the test function.")
        print("  run     : Runs the bugs.")
        print("  list    : List the available bugs.")
        print("  help    : Shows this help menu.")
        print("  exit    : exit to the main menu.")

    def help_help(self):
        print("Shows help menu.")

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
        print("list [re]*\nLists the available bugs matching the provided regex.")

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
