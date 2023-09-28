#!/usr/bin/python3
"""
This algorithm finds the peak of
a list of integers.
"""


def find_peak(list_of_integers):
    """
    This function is the peak finding algorithm
    """
    if list_of_integers == []:
        return None

    list_len = len(list_of_integers)
    my_mean = int(list_len / 2)
    nl = list_of_integers

    if my_mean - 1 < 0 and my_mean + 1 >= list_len:
        return nl[my_mean]
    elif my_mean - 1 < 0:
        return nl[my_mean] if nl[my_mean] > nl[my_mean + 1] \
            else nl[my_mean + 1]
    elif my_mean + 1 >= list_len:
        return nl[my_mean] if nl[my_mean] > nl[my_mean - 1] \
            else nl[my_mean - 1]

    if nl[my_mean - 1] < nl[my_mean] > nl[my_mean + 1]:
        return nl[my_mean]

    if nl[my_mean + 1] > nl[my_mean - 1]:
        return find_peak(nl[my_mean:])
    return find_peak(nl[:my_mean])
