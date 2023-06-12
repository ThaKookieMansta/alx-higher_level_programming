#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    A function that finds the biggest integer of a list.
    :param my_list:
    :return:
    """
    if len(my_list) == 0:
        return None

    my_max_value = 0
    for i in my_list:
        if i > my_max_value:
            my_max_value = i
    return my_max_value
