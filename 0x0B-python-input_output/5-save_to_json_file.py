#!/usr/bin/python3
"""a program that writes an Object to a text file, using a JSON representation: """
import json


def save_to_json_file(my_obj, filename):
    """
    writes json format of an object to text file
    :param my_obj: the object tobe serialized
    :param filename: the file in which the json going tobe written on
    """

    with open(filename, 'w+') as file:
        my_obj_json = json.dumps(my_obj)
        file.write(my_obj_json)
