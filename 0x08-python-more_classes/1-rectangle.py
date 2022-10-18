#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle class with 2 private instance members"""
    def __init__(self, width=0, height=0):
        """Initilizing"""
        self.width(width)
        self.height(height)

    @property
    def width(self):
        """Returns width instance variable"""
        return (self.width)

    @width.setter
    def width(self, value):
        """sets value to width instance varible"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if (isinstance(value, int)):
            self.width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Returns width instance variable"""
        return (self.height)

    @height.setter
    def height(self, value):
        """Sets value to height instance variable"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if (isinstance(int, value)):
            self.height = value
        else:
            raise TypeError("height must be an integer")
