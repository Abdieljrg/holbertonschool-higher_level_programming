#!/usr/bin/python3
"""defining the Student class and its methods for
JSON-like operations."""


class Student:
    """
    Defines a student with first name, last name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of
        a Student instance."""
        if isinstance(
                attrs, list) and all(isinstance(item, str) for item in attrs):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance based on the
        provided JSON dictionary"""
        for key, value in json.items():
            # This sets the attribute if it exists on the instance.
            if hasattr(self, key):
                setattr(self, key, value)
