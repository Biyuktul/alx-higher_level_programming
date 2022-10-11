#!/usr/bin/python3
"""Square class with private variables and methods"""


class Square:
    """Constructor"""
    def __init__(self, size=0):
        if type(sie) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    """Getter"""
    def size(self):
        return self.__size
    """Setter"""
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value 
    """Function to calculate area of a square object"""
    def area(self):
        result = self.size(self)
        return result ** 2
