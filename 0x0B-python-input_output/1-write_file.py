#!/usr/bin/python3
"""defines a function to write into text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the\
    number of characters written
    """
    with open(filename, 'w', encoding="UTF8") as file:
        return file.write(text)
