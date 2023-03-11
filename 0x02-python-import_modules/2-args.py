#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_str = "argument" if len(argv) > 1 else "arguments"
    print("{} {}:".format(len(argv) - 1, arg_str))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
