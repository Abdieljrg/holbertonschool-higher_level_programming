#!/usr/bin/python3
"""loading objects from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates object from JSON file."""
    with open(filename, 'r', encoding='UTF8') as f:
        return json.load(f)
