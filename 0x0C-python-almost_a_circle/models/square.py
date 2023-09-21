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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Gets the value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size of the square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        num_arg = 0
        if len(args) != 0 and args:
            for arg in args:
                if num_arg == 0:
                    self.id = args[0]
                elif num_arg == 1:
                    self.size = args[1]
                elif num_arg == 2:
                    self.x = args[2]
                elif num_arg == 3:
                    self.y = args[3]
                num_arg += 1
            return

        for key in kwargs:
            if key == "id":
                self.id = kwargs["id"]
            if key == "size":
                self.size = kwargs["size"]
            if key == "x":
                self.x = kwargs["x"]
            if key == "y":
                self.y = kwargs["y"]

        def to_dictionary(self):
            """Returns the dictionary representation of a Square"""
            return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

