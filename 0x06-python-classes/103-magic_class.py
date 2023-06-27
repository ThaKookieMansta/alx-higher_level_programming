#!/usr/bin/python3
"""
Module generated from a Bytecode
"""
import math


class MagicClass:
    """
    This class defines a circle object
    """
    def __init__(self, radius=0):
        """
        Instantiates the class attributes
        :param radius:
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of a circle
        :return:
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculates the circumference of a circle
        :return:
        """
        return 2 * math.pi * self.__radius
