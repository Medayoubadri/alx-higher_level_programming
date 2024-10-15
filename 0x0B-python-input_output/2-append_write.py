#!/usr/bin/python3
"""
Appends text to a file, sometimes files just aren't big enough.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF8 text file and returns the number
    of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
