import os


def list_all_files(cmd):
    return os.system(cmd)


command = 'ls'
result = list_all_files(command)
print(result)
