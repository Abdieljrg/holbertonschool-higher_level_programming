#!/usr/bin/python3
"""
function `lookup`: returns
the list of attributes and methods of an object.
"""

def lookup(obj):
    """Returns the list of attributes and methods of an object.
Returns:
        A list of attributes and methods of the object."""
    return dir(obj)
