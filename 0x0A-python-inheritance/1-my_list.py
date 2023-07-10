#!/usr/bin/python3
"""
This module includes a class that inherits
from list
"""


class MyList(list):
    """
    This class inherits from list class
    """

    def print_sorted(self):
        """
        This method prints a list in ascending order
        :return:
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
