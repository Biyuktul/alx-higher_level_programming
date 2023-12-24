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

    def to_json(self, attrs=None):
        """
        returns a dictionary representation of a class Student
        """
        if isinstance(attrs, list)\
            and all(isinstance(item, str) for item in attrs):
            result = {}
            for k in attrs:
                if hasattr(self, k):
                    result[k] = getattr(self, k)
            return result
        # or a precise way to do the above is using the dict comprehention
        # return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__
