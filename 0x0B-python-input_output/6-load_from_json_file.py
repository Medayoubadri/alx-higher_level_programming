#!/usr/bin/python3
"""
Loads a Python object from a JSON file.
Think of it as summoning an object from its JSON grave.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a “JSON file.”
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
