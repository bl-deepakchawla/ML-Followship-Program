import sys


def cmd_arguments():
    print("File names: ", sys.argv[0])
    print("No. of arguments: ", sys.argv[1])
    print("Arguments names: ", sys.argv[2:])


cmd_arguments()

