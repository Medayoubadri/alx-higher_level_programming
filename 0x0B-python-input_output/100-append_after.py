#!/usr/bin/python3
"""
Inserts a line of text to a file, after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts new_string to the file after each line containing search_string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
