#!/usr/bin/python3
"""define a function inherits_from"""


def inherits_from(obj, a_class):
    """
    determines if the object is an instance of a class\
    that inherited from the specified class
    :param obj:the object
    :param a_class: the class
    :return: True if obj is instance of a class that inherited from a_class\
    False otherwise
    """
    return issubclass(obj.__class__, a_class)
