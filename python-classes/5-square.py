#!/usr/bin/python3
""" Square """


class Square:
    """ class square """

    def __init__(self, size=0):
        """ initialize private instance square """

        self.__size = size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of square
        size setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area calculation """
        return self.__size ** 2

    def my_print(self):
        """ printing """

        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
