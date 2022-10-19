#!/usr/bin/python3
"""Rectangle Class Definition"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """initializer"""
        if (not isinstance(height, int)):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        if (not isinstance(width, int)):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if (not isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Height setter"""
        if (not isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area calculator"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter calculator"""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return The string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
