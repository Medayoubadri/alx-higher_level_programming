#!/usr/bin/python3
"""
Converts a Python object to a JSON string. It's like wrapping your object
in shiny digital packaging.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    return json.dumps(my_obj)
