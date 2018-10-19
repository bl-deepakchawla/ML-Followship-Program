import os


def absolute_file_path(path):
    return os.path.abspath(path)


path = 'your_file_path'
result = absolute_file_path(path)
print(result)
