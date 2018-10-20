import time
import os.path


def retrieve_file_properties(file_name):
    print('File Name:', file_name)
    print('Access time:', time.ctime(os.path.getatime(file_name)))
    print('Modified time:', time.ctime(os.path.getmtime(file_name)))
    print('Change time:', time.ctime(os.path.getctime(file_name)))
    print('Size in bytes:', os.path.getsize(file_name))


file_name = 'file/path'
retrieve_file_properties(file_name)
