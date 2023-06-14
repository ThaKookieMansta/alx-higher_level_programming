#!/usr/bin/python3
def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    :param a_dictionary:
    :return:
    """
    highest_value = 0
    highest_value_key = None

    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > highest_value:
                highest_value = value
                highest_value_key = key

    return highest_value_key
