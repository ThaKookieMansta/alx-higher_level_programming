#!/usr/bin/python3
"""
This module multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices
    :param m_a: Matrix 1
    :param m_b: Matrix 2
    :return: New multiplied matrix
    """

    """
    This code block is for validation, no computation
    is happening here
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if not i:
            raise ValueError("m_a can't be empty")
        for a in i:
            if not isinstance(a, (int, float)):
                raise TypeError("m_a should contain only integers or floats ")
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")
        if not j:
            raise ValueError("m_b can't be empty")
        for b in j:
            if not isinstance(b, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(j) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """
    Now we start the computation of the matrices
    """

    new_matrix = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            one_element = 0
            for k in range(len(m_a[0])):
                temp_val = m_a[i][k] * m_b[k][j]
                one_element += temp_val
            new_row.append(one_element)
        new_matrix.append(new_row)
    return new_matrix
