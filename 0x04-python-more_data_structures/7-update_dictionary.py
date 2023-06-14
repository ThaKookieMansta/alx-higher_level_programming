#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds key/value in a dictionary.
    :param a_dictionary:
    :param key:
    :param value:
    :return:
    """
    a_dictionary.update({key: value})
    return a_dictionary.copy()
