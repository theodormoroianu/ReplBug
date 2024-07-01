from typing import Dict
import progressbar
import logging

import testcase.bug_list
import testcase.bug as bug


def run_bugs(patterns: list[str]):
    """
    Runs the list of provided bugs
    """
    bugs_to_run: Dict[str, bug.Bug] = testcase.bug_list.get_bugs(patterns)
    if not bugs_to_run:
        print("No bugs found for the provided patterns.")
        return
    print(f"Running the following bugs: {', '.join(bugs_to_run.keys())}")
    logging.info(f"Running the following bugs: {', '.join(bugs_to_run.keys())}")

    progressbar.streams.wrap_stderr()
    progressbar.streams.wrap_stdout()

    for idx, bug_name in progressbar.progressbar(list(enumerate(bugs_to_run))):
        bugs_to_run[bug_name].run()

    if not bugs_to_run:
        print("No bugs found for the provided patterns.")


def test():
    pass
