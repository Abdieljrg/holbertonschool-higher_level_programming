#!/usr/bin/python3
"""appends a string to a text file. return char number of added"""


def append_write(filename="", text=""):
    """Appends a string of text file (UTF8), returns num of char added"""
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)