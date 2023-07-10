#!/usr/bin/python3

"""
This module contains a function that returns True if the
object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    :param obj: The class object
    :param a_class: The class
    :return: True if it is an instance otherwise False
    """

    return type(obj) == a_class
