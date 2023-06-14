#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
     A function that prints a dictionary by ordered keys
    :param a_dictionary:
    :return:
    """
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
