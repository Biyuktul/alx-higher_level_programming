#!/usr/bin/python3
"""a program to read and print utf-8 textfile """


def read_file(filename=""):
    """
    function to read file pointed by filename
    """
    with open(filename, 'r',  encoding="utf-8") as file_content:
        content = file_content.read()
        print(content, end="")
