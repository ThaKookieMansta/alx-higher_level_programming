#!/usr/bin/python3

"""
This module contains a class that inherits the list class
"""


class MyList(list):
    """
    This class inherits from list class
    """

    def __init__(self):
        """
        This instantiates the objects
        """
        super().__init__()

    def print_sorted(self):
        """
        This method prints a list in ascending order
        :return:
        """
        print(sorted(self))
