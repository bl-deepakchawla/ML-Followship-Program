import os


def sort_files_time():
    return os.system('ls -t')


file_names = sort_files_time()
print(file_names)
