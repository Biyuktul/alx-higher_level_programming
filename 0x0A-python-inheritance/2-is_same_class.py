#!/usr/bin/python3
"""defines a function to determine object is exactly\
an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    determines if an objects is an instance of specified class
    :param obj: the object
    :param a_class: the class
    :return: True if obj is instance of a_class, False otherwise
    """
    return (type(obj) == a_class)
