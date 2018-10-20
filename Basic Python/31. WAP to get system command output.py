import subprocess


def get_system_cmd_output(cmd):
    return subprocess.check_output(cmd, shell=True)


cmd = 'ls'
result = get_system_cmd_output(cmd)
print("Output of", cmd , "command:", result)
