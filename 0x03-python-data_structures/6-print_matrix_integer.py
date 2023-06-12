#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers.
    :param matrix:
    :return:
    """
    for i in matrix:
        j_length = len(i)
        for j in range(j_length):
            if j != j_length - 1:
                print("{:d}".format(i[j]), end=" ")
            else:
                print("{:d}".format(i[j]), end="")
        print()
