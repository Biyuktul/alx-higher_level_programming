#!/usr/bin/python3
"""defines a function to return all available\
attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of all attributes and methods of an object.
    """
    # Get a list of all attributes and methods of the object
    obj_members = dir(obj)

    return obj_members
