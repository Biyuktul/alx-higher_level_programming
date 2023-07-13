#!/usr/bin/python3
"""defines Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class to represent rectangle object"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """method to calculate area of the rectangle"""
        return (self.__size * self.__size)

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
