#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    A function that finds all multiples of 2 in a list.
    :param my_list:
    :return:
    """
    my_new_bool_list = []

    for i in my_list:
        if i % 2 == 0:
            my_new_bool_list.append(True)
        else:
            my_new_bool_list.append(False)
    return my_new_bool_list
