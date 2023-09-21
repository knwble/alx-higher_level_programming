#!/usr/bin/python3
"""Defines a base model class"""


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

        if list_dictionaries is None:
            return ("[]")
        if not type(list_dictionaries) == list:
            raise TypeError("list_dictionaries must be a list")
        for i in list_dictionaries:
            if not type(i) == dict:
                raise TypeError("Must be a list of dictionaries")

        return json.dumps(list_dictionaries)
