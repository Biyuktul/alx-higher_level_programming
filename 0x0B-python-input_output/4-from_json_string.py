#!/usr/bin/python3
"""a program that returns an object (Python data structure)
    represented by a JSON string: """
import json


def from_json_string(my_str):
    """
    function to return object representation of jason string
    :param my_str: the json string
    :return: object representation
    """
    return json.loads(my_str)
