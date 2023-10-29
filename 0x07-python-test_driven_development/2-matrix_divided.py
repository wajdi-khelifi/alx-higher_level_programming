#!/usr/bin/python3
"""Define function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divide matrix by integer, rounded to two decimal places"""
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error)
    len_row = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error)
        len_row.append(len(row))
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(error)
        row_count += 1
    if len(set(len_row)) > 1:
        raise TypeError("Each row pf the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
