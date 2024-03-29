#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """
    represents a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a dictionary representation of a class Student
        """
        return self.__dict__
