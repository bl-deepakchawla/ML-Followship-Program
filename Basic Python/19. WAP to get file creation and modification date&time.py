import os, time


def creation_modification_date_time(file_name):
    print("Creation time ", time.ctime(os.path.getctime(file_name)))
    print("Last Modification time ", time.ctime(os.path.getmtime(file_name)))


file_name = 'your_file_path'
creation_modification_date_time(file_name)
