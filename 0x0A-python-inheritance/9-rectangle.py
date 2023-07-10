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

    def area(self):
        """
        This method returns the area of the rectangle
        :return:
        """
        return self.__width * self.__height

    def __str__(self):
        """
        This str method returns a fancy string for the rectangle
        :return:
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
