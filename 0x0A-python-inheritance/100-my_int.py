#!/usr/bin/python3

"""
This module contains a class that inherits from int
"""


class MyInt(int):
    """
    This class inherits the class int
    """

    def __eq__(self, other):
        """
        This magic function defines what happens when the
        equals symbol is used in this class
        :param other:
        :return:
        """
        return int(self) != other

    def __ne__(self, other):
        """
        This magic function defines what happens when the
        not equal symbol is used in this class
        :param other:
        :return:
        """
        return int(self) == other
