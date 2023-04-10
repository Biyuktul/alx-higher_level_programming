#!/usr/bin/python3
"""define a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a new instance of the Rectangle class.
    - area(self): Calculates the area of the rectangle.
    - integer_validator(self): Validates width and height of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
