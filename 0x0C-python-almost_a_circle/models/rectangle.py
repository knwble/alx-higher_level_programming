#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # getter functions
    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y

    # setter functions
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Defines the area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """ Prints in stdout the rectangle with '#' """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print("", end=" ")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns an object string representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        num_arg = 0
        if len(args) != 0 and args:
            for arg in args:
                if num_arg == 0:
                    self.id = args[0]
                elif num_arg == 1:
                    self.__width = args[1]
                elif num_arg == 2:
                    self.__height = args[2]
                elif num_arg == 3:
                    self.__x = args[3]
                elif num_arg == 4:
                    self.__y = args[4]
                num_arg += 1
            return

        for key in kwargs:
            if key == "id":
                self.id = kwargs["id"]
            if key == "width":
                self.__width = kwargs["width"]
            if key == "height":
                self.__height = kwargs["height"]
            if key == "x":
                self.__x = kwargs["x"]
            if key == "y":
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y}
