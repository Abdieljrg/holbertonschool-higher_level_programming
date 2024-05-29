#!/usr/bin/python3
"""string to a text file, returning the number of characters"""


def write_file(filename="", text=""):
    """writes a string and returns number of char"""
    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
