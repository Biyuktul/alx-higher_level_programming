#!/usr/bin/python3
"""
This module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number
    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all([isinstance(i, list) for i in matrix]) or \
            all(isinstance(x, (int, float)) for x in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    new_list = []
    temp_list = []
    for i in range(len(matrix)):
        for v in matrix[i]:
            temp_list.append(round(v / div, ndigits=2))
        new_list.append(temp_list)
        temp_list = []

    return new_list
