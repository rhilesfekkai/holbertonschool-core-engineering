#!/usr/bin/env python3
"""Print the first x integers of a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integers from the first x elements."""
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass

    print()
    return count
