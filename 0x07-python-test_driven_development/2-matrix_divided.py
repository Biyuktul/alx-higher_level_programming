#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    a function that divides each element of a list
    of list by div and return a new list of results
    :param matrix: a list of list
    :param div: a divider
    :return: new list of list where each element rounded to 2 decimal places
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if is_list_of_lis_of_int_or_float(matrix):
        new_list = []
        if isinstance(div, (int, float)):
            for i in matrix:
                if len(i) != len(matrix[0]):
                    raise TypeError("Each row of the matrix must have the same size")
                row = []
                for j in i:
                    row.append(round(j / div, 2))
                new_list.append(row)
        else:
            raise TypeError("div must be a number")
    return new_list


def is_list_of_lis_of_int_or_float(x):
    """
    a function that checks whether a variable is a list of lists of int or float
    :param x: the variable tobe checked
    :return: True if it is, otherwise False
    """
    if isinstance(x, list):
        for i in x:
            for j in i:
                if not isinstance(j, (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats"
                    )
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return True
