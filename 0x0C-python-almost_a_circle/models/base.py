#!/usr/bin/python3

"""
This module contains the base class for the
0x0C-python-almost_a_circle project from ALX.
For more details on the class check the class
docstring
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This static method returns a JSON string
        representation of list_dictionaries
        :param list_dictionaries: This is a list of dictionaries
        :return: The JSON representation
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string list_objs into a file
        :param list_objs:
        :return:
        """

        dict_list = [i.to_dictionary() for i in list_objs]

        with open(file=f"{cls.__name__}.json", mode="w", encoding="utf-8") as my_dump:
            json.dump(dict_list, my_dump)
