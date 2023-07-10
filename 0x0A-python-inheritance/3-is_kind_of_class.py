#!/usr/bin/ python3

"""
This module contains a function that returns True if the object is an
instance of, or if the object is an instance of a class that inherited
from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    :param obj: The class object
    :param a_class: The class
    :return: True or False
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
