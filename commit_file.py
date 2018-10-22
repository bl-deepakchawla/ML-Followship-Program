import os
import sys


def create_file_commit():
    file_name = sys.argv[2]
    file_name = file_name.replace(' ', '\ ')
    os.system('touch ' +  file_name + '.py')
    os.system('git add .')
    commit_msg = 'Create Program ' + file_name[0] + ' python file'
    os.system('git commit -am \"' + commit_msg + "\"")


def commit_code_file():
    os.system('git add .')
    function_name = sys.argv[2]
    commit_msg = 'Create function ' + function_name + '()'
    os.system('git commit -am \"' + commit_msg + "\"")


if sys.argv[1] == '1':
    create_file_commit()
elif sys.argv[1] == '2':
    commit_code_file()
