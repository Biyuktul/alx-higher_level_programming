#!/usr/bin/python3
"""a program that returns the JSON representation of string object """
import json


def to_json_string(my_obj):
    """
    :param my_obj: the object tobe serialized
    :return: json representation of the object passed
    """
    return json.dumps(my_obj)
