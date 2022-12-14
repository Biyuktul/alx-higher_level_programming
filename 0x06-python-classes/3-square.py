#!/usr/bin/python3
"""Sqaure Class Having one private member and public method"""


class Square:
    """Template for Squares"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
            """Return area of a square object"""
    def area(self):
        return self.__size ** 2
