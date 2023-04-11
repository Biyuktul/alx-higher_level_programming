#!/usr/bin/python3
"""defines a function read_file to read from a file"""


def read_file(filename=""):
    """
    reads a text file and prints it to stdout
    @filename: the file name
    """
    with open(filename, 'r', encoding="UTF8") as file:
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()
