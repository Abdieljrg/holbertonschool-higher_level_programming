#!/usr/bin/python3
"""reads and prints"""


def read_file(filename=""):
    """Reads text file (UTF8) and prints out"""
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read(), end='')
