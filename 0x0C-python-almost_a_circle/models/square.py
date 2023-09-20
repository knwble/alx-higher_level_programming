#!/usr/bin/python3
"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes of the object"""

        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns an object string representation"""
        return ("[Square] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width))
