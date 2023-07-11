#!/usr/bin/python3

"""
This module contains a function that returns an object represented
by a JSON string
"""

import json


def from_json_string(my_str):
    """
    This function returns and object represented by a JSON string
    :param my_str:
    :return:
    """
    return json.loads(my_str)
