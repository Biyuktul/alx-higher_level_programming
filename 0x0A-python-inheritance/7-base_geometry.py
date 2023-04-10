#!/usr/bin/python3
"""defines BaseGeometry class"""


class BaseGeometry:
    """defines area public instance method"""
    def area(self):
        """raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        :param name: the name
        :param value: the value
        :return: void
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
