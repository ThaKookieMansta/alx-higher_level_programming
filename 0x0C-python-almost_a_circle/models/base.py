#!/usr/bin/python3

"""
This module contains the base class for the
0x0C-python-almost_a_circle project from ALX.
For more details on the class check the class
docstring
"""
import json
import csv
import turtle



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

        with open(file=f"{cls.__name__}.json", mode="w") as my_dump:
            json.dump(dict_list, my_dump)

    @staticmethod
    def from_json_string(json_string):
        """
        This method converts a JSON string into a list
        :param json_string: The JSON string to be converted
        :return: The list
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method creates instances of a class
        :param dictionary: This is a dictionary of all attributes
        :return: The instance and all attributes created
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances
        :return: The list of instances
        """
        try:
            with open(file=f"{cls.__name__}.json", mode="r") as file:
                instance_dict = cls.from_json_string(file.read())
                new_list = [cls.create(**i) for i in instance_dict]
                return new_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This method saves instance data to a csv file
        :param list_objs: The instances and their data
        :return:
        """
        with open(file=f"{cls.__name__}.csv", mode="w", newline='') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                for i in list_objs:
                    writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        This method loads instance data from a csv file
        :return:
        """
        try:
            with open(file=f"{cls.__name__}.csv", mode="r") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]

                dict_list = csv.DictReader(f=csvfile, fieldnames=fields)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in dict_list]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        This method draws the squares and rectangles
        using the turtle library
        :param list_rectangles:
        :param list_squares:
        :return:
        """
        my_pen = turtle.Turtle()
        my_pen.screen.bgcolor("yellow")
        my_pen.pensize(3)
        my_pen.shape("triangle")

        my_pen.color("black")
        for rectangle in list_rectangles:
            my_pen.showturtle()
            my_pen.up()
            my_pen.goto(rectangle.x, rectangle.y)
            my_pen.down()
            for i in range(2):
                my_pen.forward(rectangle.width)
                my_pen.left(90)
                my_pen.forward(rectangle.height)
                my_pen.left(90)
            my_pen.hideturtle()

        my_pen.color("red")
        for square in list_squares:
            my_pen.showturtle()
            my_pen.up()
            my_pen.goto(square.x, square.y)
            my_pen.down()
            for i in range(4):
                my_pen.forward(square.size)
                my_pen.left(90)
            my_pen.hideturtle()

        turtle.exitonclick()
