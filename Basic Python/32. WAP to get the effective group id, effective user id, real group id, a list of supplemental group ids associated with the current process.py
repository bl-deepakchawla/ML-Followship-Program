import os


def ids_values_of_groups():

    print("Effective ID:", os.getegid())
    print("User ID:", os.geteuid())
    print("Real Group ID:", os.getgid())
    print("Groups Names list:", os.getgroups())


ids_values_of_groups()
