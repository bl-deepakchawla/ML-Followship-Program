import os


def get_users_env():

    return os.environ


result = get_users_env()
print("Users environment variables are,", result)
