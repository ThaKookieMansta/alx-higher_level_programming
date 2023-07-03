#!/usr/biin/python3

"""
This module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix
    :param matrix:
    :param div:
    :return: Returns the divided matrix
    """
    new_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        new_row = []
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            else:
                new_val = round(j / div, 2)
            new_row.append(new_val)
        new_matrix.append(new_row)
    return new_matrix
