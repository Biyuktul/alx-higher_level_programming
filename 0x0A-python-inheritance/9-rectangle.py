#!/usr/bin/python3
"""defines Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class to represent rectangle object"""

    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """method to calculate area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
