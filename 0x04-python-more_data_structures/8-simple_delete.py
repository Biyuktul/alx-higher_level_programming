#!/usr/bin/python3
"""Simple dictionary key deletion"""


def simple_delete(a_dictionary, key=""):
    """Deletes a dictionary key"""
    keys = list(a_dictionary.keys())
    if key not in keys:
        return a_dictionary

    a_dictionary.pop(key, None)
    return a_dictionary
