#!/usr/bin/env python3
"""Define a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size after validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square position after validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) and n >= 0 for n in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # at its specified position."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the square representation as a string."""
        if self.__size == 0:
            return ""

        lines = (
            [""] * self.__position[1]
            + [
                " " * self.__position[0] + "#" * self.__size
                for _ in range(self.__size)
            ]
        )
        return "\n".join(lines)
