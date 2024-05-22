import logging
import cmd
import time

import context
import interactor.helpers as helpers


class TestcaseInteractor(cmd.Cmd):
    prompt = 'test> '
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
        import testcase.run_bugs as run_bugs
        run_bugs.test()

    def do_run(self, arg):
        """Runs the bugs."""
        import testcase.run_bugs as run_bugs
        run_bugs.run_bugs(arg.split())

    def do_bug(self, arg):
        """Runs the bugs."""
        self.do_run(arg)

    def do_help(self, arg):
        """Shows help menu."""
        print("Available commands:")
        print("test - Runs the test function.")
        print("run - Runs the bugs.")

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

