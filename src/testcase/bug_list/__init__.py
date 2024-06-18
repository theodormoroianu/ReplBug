import importlib
import pkgutil
import os
from typing import Dict
import re

import testcase.helpers as helpers
import testcase.bug as bug
import context


# Get the current package name (assuming this script is part of a package)
_package_name = __name__

_bug_list: Dict[str, bug.Bug] = dict()


def default_get_description(
    link: str,
    original_isl: helpers.IsolationLevel,
    isolation_level: helpers.IsolationLevel,
):
    return f"""
Link:                     {link}
Original isolation level: {original_isl.value}
Tested isolation level:   {isolation_level.value}
"""


# Iterate through all modules in the current package directory
for loader, module_name, is_pkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
    module = importlib.import_module(f"{_package_name}.{module_name}")
    bug_id = getattr(module, "BUG_ID")
    db_and_version = getattr(module, "DB_AND_VERSION")

    # Iterate through all isolation levels for the current database and version
    for isolation_level in helpers.isolation_levels_for_db_and_version(db_and_version):
        if "get_description" in dir(module):
            description = getattr(module, "get_description")(isolation_level)
        else:
            description = default_get_description(
                getattr(module, "LINK"),
                getattr(module, "ORIGINAL_ISOLATION_LEVEL"),
                isolation_level,
            )
        scenarios = getattr(module, "get_scenarios")(isolation_level)

        sql_setup_script = (
            context.Context.get_context().data_folder_path
            / "sql"
            / f"{bug_id}_mysql_bk.sql"
        )
        bug_runner = bug.Bug(
            bug_id=f"{bug_id}-{isolation_level.name}",
            description=description,
            db_and_type=db_and_version,
            scenarios=scenarios,
            setup_sql_script=sql_setup_script,
        )
        _bug_list[f"{bug_id}-{isolation_level.name}"] = bug_runner


def get_bugs(patterns: list[str]) -> Dict[str, bug.Bug]:
    """
    Returns the list of bugs that match the provided patterns
    """
    bugs_to_run: Dict[str, bug.Bug] = dict()

    for bug_re in patterns:
        for bug_name in _bug_list:
            if re.match(f".*{bug_re}.*", bug_name):
                bugs_to_run[bug_name] = _bug_list[bug_name]
    return bugs_to_run
