#!/usr/bin/python3
"""Defines a base model class"""
import json
import csv
import turtle
import os


class Base:
    """Represents base of all classes created """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method of the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        json_string_list = []

        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance of all attributes already set """

        if cls.__name__ == "Rectangle":
            dummy_instances = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instances = cls(1)

        dummy_instances.update(**dictionary)
        return (dummy_instances)

    @classmethod
    def load_from_file(cls):
        """ Method that returns a list of instances."""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in csv """
        desc = []
        with open(str(cls.__name__) + ".csv", mode='w') as csv_file:
            wr = csv.writer(csv_file, delimiter=',')
            if list_objs is None:
                wr.writerow(desc)
            else:
                wr.writerow(list(list_objs[0].to_dictionary().keys()))
                for instances in list_objs:
                    wr.writerow(list(instances.to_dictionary().values()))

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in csv """
        desc = []
        with open(str(cls.__name__) + ".csv", encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            flag = 0
            for row in reader:
                if flag == 0:
                    keys = row
                    flag = 1
                else:
                    row = map(lambda x: int(x), row[:])
                    desc.append(cls.create(**dict(zip(keys, row))))
            return (desc)

        if not os.path.isfile(str(cls.__name__) + ".csv"):
            raise FileNotFoundError("File not found")
            return ("[]")

    @staticmethod
    def draw(rectangles, squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            rectangles (list): A list of Rectangle objects to draw.
            squares (list): A list of Square objects to draw.
        """
        turtle_instance = turtle.Turtle()
        turtle_instance.screen.bgcolor("#E57373")
        turtle_instance.pensize(3)
        turtle_instance.shape("turtle")

        turtle_instance.color("#81C784")
        for sq in squares:
            turtle_instance.showturtle()
            turtle_instance.up()
            turtle_instance.goto(sq.x, sq.y)
            turtle_instance.down()
            for i in range(2):
                turtle_instance.forward(sq.width)
                turtle_instance.left(90)
                turtle_instance.forward(sq.height)
                turtle_instance.left(90)
            turtle_instance.hideturtle()

        turtle_instance.color("#64B5F6")
        for rect in rectangles:
            turtle_instance.showturtle()
            turtle_instance.up()
            turtle_instance.goto(rect.x, rect.y)
            turtle_instance.down()
            for i in range(2):
                turtle_instance.forward(rect.width)
                turtle_instance.left(90)
                turtle_instance.forward(rect.height)
                turtle_instance.left(90)
            turtle_instance.hideturtle()

        turtle.exitonclick()
