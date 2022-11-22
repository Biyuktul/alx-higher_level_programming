#!/usr/bin/python3
"""a program to appends utf-8 string to a text file"""


def append_write(filename="", text=""):
    """
    writes the string text into a textfile
    :param filename: the file tobe opend and modified
    :param text: the content tobe writen
    """
    with open(filename, 'a+', encoding="UTF-8") as file:
        file.write(text)
    return len(text)
