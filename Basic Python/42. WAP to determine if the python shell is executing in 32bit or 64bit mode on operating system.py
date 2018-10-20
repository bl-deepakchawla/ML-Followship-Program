import struct


def shell_32bit_64bit():
    return struct.calcsize("P") * 8


result = shell_32bit_64bit()
print(result)
