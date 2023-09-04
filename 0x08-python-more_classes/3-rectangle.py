#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Retrieves the area of the Rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """Retrieves the perimeter of the Rectangle."""
        if self.height == 0 or self.width == 0:
            return (0)

        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Returns the string representation of the sqaure."""
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return ("")

        for i in range(self.__height):
            rectangle += (('#' * self.__width) + '\n')

        return (rectangle[:-1])
