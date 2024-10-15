#!/usr/bin/python3
"""
Module that defines the class MyInt.
"""


class MyInt(int):
    """
    MyInt is a rebel. It inverts the == and != operators.
    """

    def __eq__(self, other):
        """Override the == operator to behave like !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to behave like ==."""
        return super().__eq__(other)
