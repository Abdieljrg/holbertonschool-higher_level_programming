#!/usr/bin/python3
""" Square """


class Square:
    """ class square """

    def __init__(self, size=0):
        """ initialize """
        if size != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
