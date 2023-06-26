#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    A function that prints the first x elements of a list and only integers.
    :param my_list: The list that can contain any type
    :param x: Represents the number of elements to access in the list
    :return: Returns the real numbers of integers printed
    """
    to_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            to_print += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print()
    return to_print
