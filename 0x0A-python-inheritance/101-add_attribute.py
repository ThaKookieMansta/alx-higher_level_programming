#!/usr/bin/python3

"""
This module contains a function that adds a new attribute
"""


def add_attribute(obj, attribute_name, attribute_value):
    """
    This function adds a new attribute to a class when possible
    :param obj:
    :param attribute_name:
    :param attribute_value:
    :return:
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
