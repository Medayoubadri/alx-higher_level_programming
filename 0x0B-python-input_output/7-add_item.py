#!/usr/bin/python3
"""
Adds all command-line arguments to a Python list and saves them
to a JSON file. It's like collecting things and hoarding them forever.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if __name__ == "__main__":
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, filename)
