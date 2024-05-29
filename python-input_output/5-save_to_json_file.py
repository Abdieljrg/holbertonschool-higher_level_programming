#!/usr/bin/python3
"""saving objects in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object using JSON"""
    with open(filename, 'w', encoding='UTF8') as f:
        json.dump(my_obj, f)
