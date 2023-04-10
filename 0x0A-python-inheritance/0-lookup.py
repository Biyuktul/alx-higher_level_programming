#!/usr/bin/python3
"""defines a function lookup"""


def lookup(obj):
    """
    looks for available attributes of an object
    :param obj: the object to look for
    :return: a list of available attribute and methods
    """
    return dir(obj)
