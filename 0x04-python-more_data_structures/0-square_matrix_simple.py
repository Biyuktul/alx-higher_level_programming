#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix."""
    new_matrix = []
    for i in matrix:
        mat = []
        for j in range(len(i)):
            sq = i[j] ** 2
            mat.append(sq)
        new_matrix.append(mat)
    return new_matrix
