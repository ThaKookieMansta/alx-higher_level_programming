#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    A function that deletes keys with a specific
    value in a dictionary
    :param a_dictionary:
    :param value:
    :return:
    """
    if type(a_dictionary) is dict and a_dictionary is not None:
        for_deletion = {key: val for (key, val) in a_dictionary.items() if val == value}
        for keys, vals in for_deletion.items():
            del a_dictionary[keys]
    return a_dictionary.copy()
