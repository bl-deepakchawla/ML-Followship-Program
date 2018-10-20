import sys


def size_of_object(obj_name):
    return sys.getsizeof(obj_name)


result = size_of_object("abc")
print("Size of abc is ", result, "bytes.")
