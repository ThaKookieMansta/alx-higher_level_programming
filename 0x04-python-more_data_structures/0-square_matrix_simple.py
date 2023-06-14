#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    A function that computes the square value of all integers of a matrix
    :param matrix:
    :return:
    """
    squared_matrix = []
    for i in matrix:
        squared_matrix.append(list(map(lambda x: x ** 2, i)))
    return squared_matrix
