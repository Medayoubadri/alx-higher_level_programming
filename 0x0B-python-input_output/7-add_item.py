#!/usr/bin/python3
"""
A script that adds command-line arguments to a list and saves them to a file.
Because who doesn't love keeping track of all their arguments in a JSON file?
"""


import sys
import os.path

# Import the functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
