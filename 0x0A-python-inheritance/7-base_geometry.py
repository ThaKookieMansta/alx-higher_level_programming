#!/usr/bin/python3

"""
This module contains an empty class
"""


class BaseGeometry:
    """
    This is an empty class
    """

    def area(self):
        """
        This method calculates the area
        :return:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates the value
        :param name:
        :param value:
        :return:
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
