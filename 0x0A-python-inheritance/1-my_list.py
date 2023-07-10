#!/usr/bin/python3

"""
This module includes a class that inherits
from list
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
