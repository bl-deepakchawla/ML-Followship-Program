import timeit


def power_function():
    pow(20, 2)


def function_time_taken():
    return timeit.timeit(power_function)


time_taken = function_time_taken()
print(time_taken, 'seconds')