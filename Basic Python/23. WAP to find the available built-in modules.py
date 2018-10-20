import sys


def built_in_modules():
    return sys.builtin_module_names


modules_name = built_in_modules()
print("Module names:", ", ".join(modules_name))
