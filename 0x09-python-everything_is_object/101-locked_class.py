#!/usr/bin/python3
"""defines a class LockedClass"""


class LockedClass:
    """
    that prevents the user from dynamically creating\
    new instance attributes
    """
    __slots__ = "first_name"
