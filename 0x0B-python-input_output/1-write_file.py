#!/usr/bin/python3
"""a program to writes utf-8 string to a text file"""


def write_file(filename="", text=""):
    """
    writes the string text into a textfile
    :param filename: the file tobe opend and modified
    :param text: the content tobe writen
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        file.write(text)
    return len(text)

