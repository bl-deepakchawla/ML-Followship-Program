import os


def access_env_variables(env_value):
    return os.environ[env_value]


env_variable = 'HOME'
result = access_env_variables(env_variable)
print(result)
