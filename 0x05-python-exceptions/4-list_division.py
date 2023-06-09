#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    This function divides 2 lists element by element
    :param my_list_1: The first list that can contain any type
    :param my_list_2: The second list that can contain any type
    :param list_length:
    :return: A new list with all divisions
    """
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            continue
    return new_list
