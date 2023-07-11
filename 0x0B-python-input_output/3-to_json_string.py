#!/usr/bin/python3

"""
This module contains a function that converts string to json
"""

import json


def to_json_string(my_obj):
    """
    This function converts string to json
    :param my_obj:
    :return: json
    """
    return json.dumps(my_obj)
