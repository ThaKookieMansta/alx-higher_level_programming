#!/usr/bin/python3
"""
This module contains a lookup function that will print all available
attributes of an object
"""


def lookup(obj):
    """
    This function prints out a list of attributes of a class object
    :param obj: The class object.
    :return: The list of attributes and methods
    """
    return dir(obj)
