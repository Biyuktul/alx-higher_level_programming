#!/usr/bin/python3
"""defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    determine whether an object is a subclass of a specified class or not
    :param obj: the object
    :param a_class: the class
    :return: True if obj is subclass of a_class, False otherwise
    """
    return issubclass(obj.__class__, a_class)

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))