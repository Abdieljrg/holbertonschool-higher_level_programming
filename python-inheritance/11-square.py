#!/usr/bin/python3
"""square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square."""

    def __init__(self, size):
        """Square instance with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes area of square"""
        return self.__size ** 2

    def __str__(self):
        """string representation of square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def print(self):
        """Prints the description of the square"""
        print(str(self))
