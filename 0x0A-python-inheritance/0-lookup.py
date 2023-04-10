#!/usr/bin/python3
"""defines a function to return all available\
attributes and methods of an object"""


def lookup(obj):
    """
    looks for available attributes of an object
    :param obj: the object to look for
    :return: a list of available attribute and methods
    """
    return list(dir(obj))
