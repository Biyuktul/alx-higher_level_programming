#!/usr/bin/python3
"""defines a function class_to_json"""


def class_to_json(obj):
    """
    a function that takes an object as input, and returns a dictionary\
    representation of that object that can be easily serialized to JSON
    """
    return obj.__dict__
