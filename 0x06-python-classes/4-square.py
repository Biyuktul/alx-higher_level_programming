#!/usr/bin/python3
"""
this module defines a square class
"""


class Square:
    """
    this class defines a Square blueprint
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        method to calculate area of the square
        :return: area of the square
        """
        return self.__size * self.__size
