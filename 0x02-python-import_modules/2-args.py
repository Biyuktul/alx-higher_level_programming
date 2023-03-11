#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_str = ''
    if len(argv) == 1:
        arg_str = 'arguments.'
    elif len(argv) > 2:
        arg_str = 'arguments:'
    else:
        arg_str = 'argument:'

    print("{} {}".format(len(argv) - 1, arg_str))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
