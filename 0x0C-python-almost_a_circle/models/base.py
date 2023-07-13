#!/usr/bin/python3

"""
This module contains the base class for the
0x0C-python-almost_a_circle project from ALX.
For more details on the class check the class
docstring
"""


class Base:
    """
    This is the base class for the 0x0C-python-almost_a_circle project
    from ALX. The goal of it is to manage id attribute in all your
    future classes and to avoid duplicating the same code
    (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This instantiates the class Base and sets an instance ID
        :param id: The ID for the instances created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
