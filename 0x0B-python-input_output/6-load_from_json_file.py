#!/usr/bin/python3
"""a program that creates an Object from a “JSON file”: """
import json


def load_from_json_file(filename):
    """
    creates a python object from json file
    :param filename: the json file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
