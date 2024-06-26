#!/usr/bin/python3
"""rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle."""

    def __init__(self, width, height):
        """Rectangle instance with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        """Prints description of rectangle"""
        print(str(self))
