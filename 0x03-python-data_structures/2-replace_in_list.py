#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Function replaces the element of a list in a specific position
    :param my_list:
    :param idx:
    :param element:
    :return:
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    my_list[idx] = element
    return my_list
