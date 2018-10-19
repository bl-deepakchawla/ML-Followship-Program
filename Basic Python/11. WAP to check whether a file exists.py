import os


def file_exist(file_name):
    print("File exists") if os.path.isfile(file_name) else print("File not exists")


file_name = "path/your_file_name"
file_exist(file_name)