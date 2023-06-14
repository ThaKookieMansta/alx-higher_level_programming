#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary
    :param a_dictionary:
    :param key:
    :return:
    """

    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary.copy()