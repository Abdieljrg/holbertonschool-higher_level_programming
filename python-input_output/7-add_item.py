#!/usr/bin/python3
"""scrip that adds all arguments to list and save """


import sys


if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    """loads and save"""

try:
    data = load_from_json("add_item.json")
except FileNotFoundError:
    data = []

for arg in sys.argv[1:]:
    data.append(arg)

save_to_json(data, "add_item.json")
