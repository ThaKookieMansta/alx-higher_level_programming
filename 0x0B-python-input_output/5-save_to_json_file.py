#!/usr/bin/python3

"""
This module contains a function that writes an Object to a text file
using a JSON Representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation
    :param my_obj:
    :param filename:
    :return:
    """
    with open(filename, mode="w", encoding="utf-8") as text_file:
        json.dump(my_obj, text_file)
