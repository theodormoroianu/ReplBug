import importlib
import pkgutil
import os
from typing import Dict

import testcase.bug as bug

# Get the current package name (assuming this script is part of a package)
package_name = __name__

bug_list: Dict[str, bug.Bug] = dict()

# Iterate through all modules in the current package directory
for loader, module_name, is_pkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
    module = importlib.import_module(f"{package_name}.{module_name}")
    try:
        get_bugs = getattr(module, "get_bug_scenarios")()
        for bug_name in get_bugs:
            assert bug_name not in bug_list, f"Duplicate bug name: {bug_name}"
            bug_list[bug_name] = get_bugs[bug_name]
    except AttributeError:
        pass