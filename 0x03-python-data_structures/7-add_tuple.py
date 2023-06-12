#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    A function that adds 2 tuples.
    :param tuple_a:
    :param tuple_b:
    :return:
    """

    if len(tuple_a) < 2 or len(tuple_b) < 2:
        list_a = list(tuple_a)
        list_b = list(tuple_b)
        for i in range(2):
            list_a.append(0)
            list_b.append(0)
        tuple_a = tuple(list_a)
        tuple_b = tuple(list_b)
    tup_val_0 = tuple_a[0] + tuple_b[0]
    tup_val_1 = tuple_a[1] + tuple_b[1]
    new_tup = (tup_val_0, tup_val_1,)
    return new_tup
