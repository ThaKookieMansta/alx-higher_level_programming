#!/usr/bin/python3

"""
This module prints a square using the # symbol
"""


def print_square(size):
    """
    This function prints a square with the # symbol
    :param size: The length of the square
    :return: The image
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    square_height = size
    for i in range(size):
        while square_height:
            print("#" * size)
            square_height -= 1
