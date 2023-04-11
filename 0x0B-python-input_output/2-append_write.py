#!/usr/bin/python3
"""defines a function append_write that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)\
    and returns the number of characters added:
    """
    with open(filename, 'a', encoding="UTF8") as file:
        return file.write(text)
