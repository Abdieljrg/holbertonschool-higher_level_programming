#!/usr/bin/python3
"""scrip to do a command line args and save i to JSON File"""

import sys
import json

# import
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# the file for saving
filename = "add_item.json"

try:
    # existing data to file
    items = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    """If the file doesn't exist or contains invalid JSON,
    start with an empty list"""
    items = []

"""Extend the list with the arguments provided on the
command line (excluding the script name)"""
items.extend(sys.argv[1:])

# Saving list
save_to_json_file(items, filename)
