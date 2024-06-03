from typing import Dict
import testcase.bug_list
import re
import testcase.bug as bug
import logging


def run_bugs(bugs: list[str]):
    """
    Runs the list of provided bugs
    """
    bugs_to_run: Dict[str, bug.Bug] = dict()

    for bug_re in bugs:
        found = False
        for bug_name in testcase.bug_list.bug_list:
            if re.match(bug_re, bug_name):
                bugs_to_run[bug_name] = testcase.bug_list.bug_list[bug_name]
                found = True
        if not found:
            logging.info("No bugs found for the provided regex: %s", bug_re)

    logging.info(f"Running the following bugs: {', '.join(bugs_to_run.keys())}")
    for bug_name in bugs_to_run:
        bugs_to_run[bug_name].run()

    if not bugs_to_run:
        print("No bugs found for the provided patterns.")

    input("Press enter to exit...")


def test():
    pass
