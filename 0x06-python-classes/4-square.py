#!/usr/bin/python3
"""Square class with private variables and methods"""


class Square:
    """Constructor"""
    def __init__(self, size=0):
        size(size)
    """Getter"""
    def size():
        return self.__size
    """Setter"""
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
    """Function to calculate area of a square object"""
    def area(self):
        result = size()
        return result ** 2
