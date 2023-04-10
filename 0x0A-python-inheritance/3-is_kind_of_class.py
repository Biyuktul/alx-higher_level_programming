#!/usr/bin/python3
"""defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    determine whether an object is a subclass of a specified class or not
    :param obj: the object
    :param a_class: the class
    :return: True if obj is subclass of a_class, False otherwise
    """
    return isinstance(obj, a_class)
