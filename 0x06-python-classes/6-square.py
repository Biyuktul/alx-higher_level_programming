#!/usr/bin/python3
"""
this module defines a square class
"""


class Square:
    """
    this class defines a Square blueprint
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = value

    def area(self):
        """
        method to calculate area of the square
        :return: area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        print the square instance using the # character
        :return: Void
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
