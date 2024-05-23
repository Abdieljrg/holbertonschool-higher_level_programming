#!/usr/bin/python3
"""inherits_from."""


def inherits_from(obj, a_class):
    """object is an instance of a class that inherited
    from the specified class = true, otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
