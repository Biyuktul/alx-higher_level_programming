#!/usr/bin/python3
"""definess rectangle class"""


class Rectangle:
    """class to represent rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method to caculate area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """method to calculate perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        square = ""
        for i in range(self.__height):
            row = ""
            for j in range(self.__width):
                row += "#"
            if i < self.__height - 1:
                row += "\n"
            square += row
        return square
