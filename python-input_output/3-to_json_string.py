#!/usr/bin/python3
"""Python objects to JSON strings"""

import json


def to_json_string(my_obj):
    """JSON string of a Python object."""
    return json.dumps(my_obj)
