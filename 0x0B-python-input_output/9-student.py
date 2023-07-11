#!/usr/bin/python3


"""
This module contains a class Student
"""


class Student:
    """
    The Class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        This function instantiates the class variables
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This function retrieves a dictionary representation
        of a Student instance
        :return:
        """
        return self.__dict__
