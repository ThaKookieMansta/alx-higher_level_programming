#!/usr/bin/python3

"""
This module prints your name in a sentence
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints your name in a sentence
    :param first_name:
    :param last_name:
    :return: The sentence My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
