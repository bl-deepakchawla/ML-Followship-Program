import os


def external_command(cmd):
    return os.system(cmd)


command = 'ls'
result = external_command(command)
print(result)
