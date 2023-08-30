#!/usr/bin/python3
import math


class MagicClass:
    

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Declares a method that returns an operation."""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Declares a method that returns an operation."""
        return ((2 * math.pi) * self.__radius)

