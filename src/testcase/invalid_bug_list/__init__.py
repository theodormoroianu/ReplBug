import os
from typing import Dict

import testcase.bug as bug
import testcase.load_bugs as load_bugs


def get_bugs(patterns: list[str]) -> Dict[str, bug.Bug]:
    """
    Returns the list of bugs that match the provided patterns
    """
    bugs = load_bugs.load_bugs_from_module(os.path.dirname(__file__), __name__, False)

    return load_bugs.get_bugs(bugs, patterns)
