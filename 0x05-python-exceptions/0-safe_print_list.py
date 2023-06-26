#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    This function prints x elements of a list
    :param my_list: A list of any type
    :param x: Represents teh number of elements to print
    :return: The real number of elements printed
    """
    to_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            to_print += 1
        except:
            continue
    print()
    return to_print
