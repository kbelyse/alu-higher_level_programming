#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square with a given size."""
        self.size = size  # Use the setter to validate size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private attribute

    def area(self):
        """Return the current square area."""
        return self.__size ** 2  # Area calculation

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
        else:
            for _ in range(self.__size):
                print("#" * self.__size)  # Print the square
