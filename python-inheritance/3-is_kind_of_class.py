#!/usr/bin/python3
"""is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """True if object is an instance, or if the object is an instance
    of a class that inherited from the specified class. if else False. """
    return isinstance(obj, a_class)
