#!/usr/bin/python3

def element_at(my_list, idx):
    """
    This function retrieves an element from a list
    :param my_list: The list
    :param idx:
    :return:
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]
