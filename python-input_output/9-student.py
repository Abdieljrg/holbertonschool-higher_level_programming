#!/usr/bin/python3
"""defining the Student class"""


class Student:
    """student name, last name, and age attributes."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of Student instance"""
        # This could also be done by directly returning self.__dict__,
        # but we explicitly list the attributes for clarity and control.
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
