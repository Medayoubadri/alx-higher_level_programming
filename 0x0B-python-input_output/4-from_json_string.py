#!/usr/bin/python3
"""
Converts a JSON string into a Python object. It's like opening
that neatly wrapped digital gift.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.
    """
    return json.loads(my_str)
