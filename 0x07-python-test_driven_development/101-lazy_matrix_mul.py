#!/usr/bin/python3
"""
This module multiplies matrices using the numpy module
"""

from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices
    :param m_a: Matrix 1
    :param m_b: Matrix 2
    :return: The new matrix
    """
    return matmul(m_a, m_b)
