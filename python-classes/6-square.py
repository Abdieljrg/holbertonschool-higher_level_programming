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

    @property
    def position(self):
        """ Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area calculation """
        return self.__size ** 2

    def my_print(self):
        """ printing """

        if self.__size == 0:
            print("")
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)