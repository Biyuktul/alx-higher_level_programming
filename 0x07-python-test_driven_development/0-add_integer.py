#!/usr/bin/python3
"""this module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):

    """ Function that adds two integer and/or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
