#!/usr/bin/python3
"""defines Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
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
