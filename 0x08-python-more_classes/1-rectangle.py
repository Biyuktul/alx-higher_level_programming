#!/usr/bin/python3
"""Rectangle Class Definition"""


class Rectangle:
    """Rectangle class with 2 private instance members"""
    def __init__(self, width=0, height=0):
        """initializer"""
        if (not isinstance(width, int)):
            raise TypeError("width must an integer")
        if (width < 0):
            raise ValueError("Width must be >= 0")
        else:
            self.__width = width

        if (not isinstance(height, int)):
            raise TypeError("height must an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.height = height

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter"""
        if (not isinstance(value, int)):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
