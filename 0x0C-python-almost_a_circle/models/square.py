#!/usr/bin/python3

"""
This module contains the Square class for all
square instances that may be created
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    This is the square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This method instantiates the Square instances
        :param size:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(size, size, x, y, id )

    def __str__(self):
        """
        This magic method returns the fancy text for this class
        :return:
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
