import socket


def get_host_name():
    return socket.gethostname()


result = get_host_name()
print("Running host name:", result)
