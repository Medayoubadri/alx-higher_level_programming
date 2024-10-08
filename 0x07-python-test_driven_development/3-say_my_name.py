#!/usr/bin/python3
"""
This module provides a function that prints
'My name is <first name> <last name>'.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name to print.
        last_name (str, optional):
            The last name to print. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Handle the special case where both first_name and last_name are empty
    if first_name == "" and last_name == "":
        print("My name is ")
    elif last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
