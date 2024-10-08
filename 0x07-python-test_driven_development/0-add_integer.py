#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """Adds two integers. Casts floats to integers."""

    if isinstance(a, float):
        if a != a:
            raise ValueError("cannot convert float NaN to integer")
        if a == float('inf') or a == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float):
        if b != b:
            raise ValueError("cannot convert float NaN to integer")
        if b == float('inf') or b == float('-inf'):
            raise OverflowError("cannot convert float infinity to integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
