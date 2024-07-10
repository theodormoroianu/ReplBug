from typing import Dict
import progressbar
import logging

import testcase.bug_list
import testcase.invalid_bug_list
import testcase.bug as bug


def run_bugs(patterns: list[str]):
    """
    Runs the list of provided bugs. It considers both valid and invalid bugs.
    The bugs are ran in the order they are found in the bug_list and invalid_bug_list,
    and the results are placed in the `results/` and `invalid_results/` folders.

    :param patterns: A list of patterns to match the bugs to run.
    """
    bugs_to_run: Dict[str, bug.Bug] = testcase.bug_list.get_bugs(patterns)
    invalid_bugs_to_run: Dict[str, bug.Bug] = testcase.invalid_bug_list.get_bugs(
        patterns
    )

    for bug_name in invalid_bugs_to_run:
        assert bug_name not in bugs_to_run, f"Bug {bug_name} is both valid and invalid."
        bugs_to_run[bug_name] = invalid_bugs_to_run[bug_name]

    if not bugs_to_run and not invalid_bugs_to_run:
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
