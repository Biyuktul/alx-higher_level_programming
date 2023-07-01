#!/usr/bin/python3
"""defines a function matrix_divided"""



def matrix_divided(matrix, div):
  """
  function that divides each element of a list
  of list by div and return a new list of list of result
  :param matrix: a list of list
  :param div: a divider
  :return: new list of list where each element rounded to 2 decimal places
  """

  if not (isinstance(matrix, list) and all(
    [isinstance(x, list) and isinstance(y, (int, float)) for x in matrix for y in x])):
    raise TypeError(
      'matrix must be a matrix (list of lists) of integers/floats')

  if not check_row_size(matrix):
    raise TypeError('Each row of the matrix must have the same size')

  if not isinstance(div, (int, float)):
    raise TypeError('div must be a number')
  if div == 0:
      raise ZeroDivisionError('division by  zero')

  new_matrix = []
  for i in matrix:
    row = []
    for j in i:
        row.append(round(j / 3, 2))
    new_matrix.append(row)

  return new_matrix

def check_row_size(matrix):
  """
  a function to check row size
  :param matrix: a list of list
  :return: True if row size are equal, False otherwise
  """
  size = len(matrix[0])
  for i in matrix:
    if len(i) != size:
      return False
  return True
