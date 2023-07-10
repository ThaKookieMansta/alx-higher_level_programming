#!/usr/bin/python3

"""
This module contains an empty class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class Rectangle inherits from class Base Geometry
    """

    def __init__(self, width, height):
        """
        Instantiate the variables
        :param width:
        :param height:
        """
        self.integer_validator(name="width", value=width)
        self.__width = width
        self.integer_validator(name="height", value=height)
        self.__height = height
