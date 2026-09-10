#!/usr/bin/env python3
"""Print an integer."""


def safe_print_integer(value):
    """Print an integer and return True, otherwise return False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
