#!/usr/bin/python3
"""a module defines a Rectangle class"""


class Rectangle:
    """
    this class represents a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
       Args:
           width (int): The width of the rectangle.
           height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of a rectangle"""
        result = 0
        if self.__width != 0 and self.__height != 0:
            result = 2 * (self.__width + self.__height)
        return result

    def __str__(self):
        """prints the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        square = []
        for i in range(self.__height):
            for j in range(self.__width):
                square.append("#")
            if i != self.__height - 1:
                square.append("\n")
        return "".join(square)

    def __repr__(self):
        """used to recreate a Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """detects deletion of a rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
