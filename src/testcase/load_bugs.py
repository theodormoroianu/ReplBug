"""
This module helps loading bugs from a folder (i.e. bug_list).

It is used for loading the valid and the invalid bugs, and placing them in a
map that can be used for running the bugs.
"""

import enum
import importlib
import pkgutil
import re
from typing import Callable, Dict, Optional, Union

import context
import testcase.bug as bug
from testcase.helpers import IsolationLevel
import testcase.helpers as helpers


def _default_get_description(
    link: str,
    original_isl: IsolationLevel,
    isolation_level: IsolationLevel,
    bug_description: Optional[str] = None,
):
    return f"""
Link:                     {link}
Original isolation level: {original_isl.value}
Tested isolation level:   {isolation_level.value}
""" + (
        f"Description:              {bug_description}\n" if bug_description else ""
    )


def load_bugs_from_module(
    folder_path: str, package_name: str, is_valid=True
) -> Dict[str, bug.Bug]:
    """
    Load bugs from modules, given the folder path and the package name.

    :param folder_path: The path to the folder containing the modules.
    :param package_name: The name of the package containing the modules.
    :param is_valid: If false, then the bug is considered invalid.
    """
    bugs = dict()

    # Iterate through all modules in the current package directory
    for loader, module_name, is_pkg in pkgutil.iter_modules([folder_path]):
        module = importlib.import_module(f"{package_name}.{module_name}")
        bug_id = getattr(module, "BUG_ID")
        db_and_version = getattr(module, "DB_AND_VERSION")

        # Check if we need to restart the server after each request.
        kill_server_after_testcase = False
        if "KILL_SERVER_AFTER_TESTCASE" in dir(module):
            kill_server_after_testcase = getattr(module, "KILL_SERVER_AFTER_TESTCASE")

        # Get the SQL setup script. It can be in the file of in a file.
        sql_setup_script = None
        if "SETUP_SQL_SCRIPT" in dir(module):
            sql_setup_script = getattr(module, "SETUP_SQL_SCRIPT")
        else:
            sql_setup_script_path = (
                context.Context.get_context().data_folder_path
                / "sql"
                / f"{bug_id}_mysql_bk.sql"
            )
            if sql_setup_script_path.exists():
                sql_setup_script = open(sql_setup_script_path, "r").read()

        # Iterate through all isolation levels for the current database and version
        for isolation_level in helpers.isolation_levels_for_db_and_version(
            db_and_version
        ):
            if "get_description" in dir(module):
                description = getattr(module, "get_description")(isolation_level)
            else:
                description = _default_get_description(
                    getattr(module, "LINK"),
                    getattr(module, "ORIGINAL_ISOLATION_LEVEL"),
                    isolation_level,
                    (
                        getattr(module, "DESCRIPTION")
                        if "DESCRIPTION" in dir(module)
                        else None
                    ),
                )
            scenarios = getattr(module, "get_scenarios")(isolation_level)

            bug_runner = bug.Bug(
                bug_id=f"{bug_id}-{isolation_level.name}",
                description=description,
                db_and_type=db_and_version,
                scenarios=scenarios,
                setup_sql_script=sql_setup_script,
                is_valid=is_valid,
                kill_server_after_testcase=kill_server_after_testcase,
            )
            bugs[f"{bug_id}-{isolation_level.name}"] = bug_runner
    return bugs


def get_bugs(bugs: Dict[str, bug.Bug], patterns: list[str]) -> Dict[str, bug.Bug]:
    """
    Returns the list of bugs that match the provided patterns
    """
    bugs_to_run: Dict[str, bug.Bug] = dict()

    for bug_re in patterns:
        for bug_name in bugs:
            if re.match(f".*{bug_re}.*", bug_name):
                bugs_to_run[bug_name] = bugs[bug_name]
    return bugs_to_run
