
#!/usr/bin/python3
# 4-square.py
"""A module that defines a square """


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        """Declares the method where the square is printed in stdout with #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
