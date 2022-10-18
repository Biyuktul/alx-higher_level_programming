#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return (self.width)

    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if (isinstance(value, int)):
            self.width = value
        else:
            raise TypeError("width must be an integer")

    def height(self):
        return (self.height)

    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if (isinstance(int, value)):
            self.height = value
        else:
            raise TypeError("height must be an integer")
