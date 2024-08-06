"""
This module contains the replicated bugs, one bug per file.

The recognised variables declared in files are:
    - ORIGINAL_ISOLATION_LEVEL: The original isolation level of the bug.
    - BUG_ID: The bug id.
    - LINK: The link to the bug tracker.
    - DB_AND_VERSION: The database and version where the bug was found.
    - DESCRIPTION: The description of the bug.
    - SETUP_SQL_SCRIPT: The SQL script used for setting up the environment.
    - CREATE_NEW_SERVER_FOR_TESTCASE: If a new server should be created for each testcase.
    - KILL_SERVER_AFTER_TESTCASE: If the server should be stopped after running each testcase (e.g. invalid ends up in an state).
    - CUSTOM_SERVER_ARGS: The custom arguments to be passed to the server.

Additionally, the following functions are recognised:
    - get_scenarios(isolation_level: IsolationLevel): Returns a list of scenarios for the given isolation level.
    - get_description(isolation_level: IsolationLevel): Returns the description for the given isolation level.

If no sql setup script is provided, the module will look for a file with the name {bug_id}_mysql_bk.sql in the data/sql folder.
"""

import os
from typing import Dict

import testcase.bug as bug
import testcase.load_bugs as load_bugs


def get_bugs(patterns: list[str]) -> Dict[str, bug.Bug]:
    """
    Returns the list of bugs that match the provided patterns
    """
    bugs = load_bugs.load_bugs_from_module(os.path.dirname(__file__), __name__)

    return load_bugs.get_bugs(bugs, patterns)
