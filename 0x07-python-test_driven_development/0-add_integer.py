#!/usr/bin/python3
"""
a module containing a function that adds two integers
"""


def add_integer(a, b=98):
    """
    adds two integers and returns the result
    :param a: first number
    :param b: second number
    :return: sum of the two numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
