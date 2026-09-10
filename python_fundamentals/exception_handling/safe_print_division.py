#!/usr/bin/env python3
"""Safely divide two integers."""


def safe_print_division(a, b):
    """Divide a by b and print the result."""
    result = None

    try:
        result = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
