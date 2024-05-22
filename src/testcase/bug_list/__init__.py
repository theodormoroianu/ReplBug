import importlib
import pkgutil
import os

# Get the current package name (assuming this script is part of a package)
package_name = __name__

bug_list = dict()

# Iterate through all modules in the current package directory
for loader, module_name, is_pkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
    module = importlib.import_module(f"{package_name}.{module_name}")
    bug_list[module_name] = getattr(module, module_name)
