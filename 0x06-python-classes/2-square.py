#!/usr/bin/python3

class Square:
    """This is a class defining a square.
    """
    def __init__(self, size=0):
        """Declares the method where the size of the sqaure is defined.
        Args:
            param1 (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
