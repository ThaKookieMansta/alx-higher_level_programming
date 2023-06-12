#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    This function that replaces an element in a list at a specific position without modifying the original list
    :param my_list:
    :param idx:
    :param element:
    :return:
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    my_new_list = my_list.copy()
    my_new_list[idx] = element
    return my_new_list
