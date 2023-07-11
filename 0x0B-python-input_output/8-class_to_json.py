#!/usr/bin/python3

"""
This module contains a function that returns a dictionary
description with simple data structure
"""


def class_to_json(obj):
    """
    This function returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    :param obj:
    :return:
    """
    return obj.__dict__
