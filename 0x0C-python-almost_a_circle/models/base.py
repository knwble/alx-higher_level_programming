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
