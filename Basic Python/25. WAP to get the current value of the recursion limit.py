import sys


def recursion_limit_value():
    return sys.getrecursionlimit()


result = recursion_limit_value()
print("Recursion Limit value is ", result)
