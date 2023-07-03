#!/usr/bin/python3
"""
This module adds 2 integers
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers returning their sum
    :param a:
    :param b: Default is 98
    :return: The sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
