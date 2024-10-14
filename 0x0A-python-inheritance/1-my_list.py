#!/usr/bin/python3
"""
A class that inherits from list and adds a method to print the list sorted.
"""


class MyList(list):
    """
    Inherits from list and adds the print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
