#!/usr/bin/python3
"""defines base class"""
import json
import os


class Base:
    """represents base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method to creates JSON string representation of dictionary

        Args:
            list_dictionaries: the dictionary

        Returns:
            json representation of the dictionary
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method to write the JSON string representation of list_objs to a file

        Args:
            list_objs: a list of instances who inherits of Base

        Returns:
            Void
        """
        if not list_objs:
            with open(cls.__name__ + ".json", "w", encoding="UTF8") as f:
                f.write("[]")
        else:
            my_list = []
            for i in list_objs:
                my_dict = i.to_dictionary()
                my_list.append(my_dict)
            json_data = Base.to_json_string(my_list)
            with open(cls.__name__ + ".json", "w", encoding="UTF8") as f:
                f.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """
        method to create list representation of JSON string

        Args:
           json_string: is a string representing a list of dictionaries

        Returns:
           list of dictionaries
        """
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class with attributes set based
        on the provided dictionary.

        Args:
            **dictionary: Arbitrary keyword arguments
            representing the attributes and their values.

        Returns:
            An instance of the class with attributes set
            according to the provided
            dictionary.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file and return a list of instances.

        Returns:
            A list of instances of the class, loaded from the file.
        """
        if not os.path.exists(cls.__name__ + ".json"):
            return []

        with open(cls.__name__ + ".json", "r", encoding="UTF8") as f:
            new_list = []
            data = json.load(f)
            for i in data:
                new_list.append(cls.create(**i))
            return new_list
