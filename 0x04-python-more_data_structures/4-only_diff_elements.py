#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    A function that returns a set of all elements present in only one set
    :param set_1:
    :param set_2:
    :return:
    """
    return (set_1 | set_2) - (set_1 & set_2)
