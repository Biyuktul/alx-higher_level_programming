#!/usr/bin/python3
"""Rectangle Class Definition"""


class Rectangle:
    """Rectangle class with 2 private instance members"""
    def __init__(self, width=0, height=0):
        """initializer"""
        if width < 0:
            raise ValueError("width must be >= 0")
        if (isinstance(width, int)):
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")
        if (isinstance(height, int)):
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if (isinstance(value, int)):
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if (isinstance(value, int)):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
