#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Function reverses the elements in a list and prints them line by line
    :param my_list:
    :return:
    """
    my_list.reverse()
    for i in my_list:
        print("{}".format(i))
