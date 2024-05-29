#!/usr/bin/python3
"""Defining the Student class"""


class Student:
    """Name, last name, and age attributes."""
    def __init__(self, first_name, last_name, age):
        """Initializes Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            # Return only the specified attributes in attrs if all items in attrs are strings
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        else:
            # Return all attributes if attrs is not a list of strings
            return self.__dict__
