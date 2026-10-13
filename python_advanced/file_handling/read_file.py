#!/usr/bin/env python3
"""Read a UTF-8 text file and print its contents."""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
