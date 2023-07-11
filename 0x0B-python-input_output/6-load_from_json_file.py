#!/usr/bin/python3

"""
This module contains a function that creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    This function creates an Object from a JSON file
    :param filename:
    :return:
    """
    with open(filename, encoding="utf-8") as json_file:
        return json.load(json_file)
