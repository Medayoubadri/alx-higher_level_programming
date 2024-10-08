#!/usr/bin/python3
"""
This module provides a function that adds two new lines after certain characters.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    text = text.strip()

    if len(text) == 0:
        return

    chars = ['.', '?', ':']
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in chars:
            result = result.rstrip(' ')
            result += "\n\n"
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result, end="")
