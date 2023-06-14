#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    A function that returns the weighted average of all integers tuple
    :param my_list:
    :return:
    """
    if len(my_list) == 0:
        return 0
    multiplied = [score*weight for (score, weight) in my_list]
    divided = sum(multiplied) / sum(weight for (score, weight) in my_list)
    return divided
