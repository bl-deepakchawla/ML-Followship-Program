import os


def current_user():
    return os.environ['USER']


result = current_user()
print(result)
