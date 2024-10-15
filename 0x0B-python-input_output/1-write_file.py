#!/usr/bin/python3
"""
Reads a file and prints it—because printing is basically
just screaming at the screen.
"""


def write_file(filename="", text=""):
    """
    Reads a UTF8 text file and prints it to stdout.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
