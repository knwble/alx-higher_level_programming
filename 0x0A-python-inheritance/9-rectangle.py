#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry. """

    def __init__(self, width, height):
        """ Constructor method """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ Returns the area of the Rectangle. """

        return (self.__width * self.__height)

    def __str__(self):
        """ Prints rectangle's information """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
