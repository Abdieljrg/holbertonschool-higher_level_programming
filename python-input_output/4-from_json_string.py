#!/usr/bin/python3
"""converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """Python object by JSON string"""
    return json.loads(my_str)
