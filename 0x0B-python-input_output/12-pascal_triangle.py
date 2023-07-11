#!/usr/bin/python3
"""
This module contains a function that returns a list of
integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal’s triangle of n
    :param n:
    :return:
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        pt1 = triangle[-1]
        pttmp = [1]
        for i in range(len(pt1) - 1):
            pttmp.append(pt1[i] + pt1[i + 1])
        pttmp.append(1)
        triangle.append(pttmp)
    return triangle
