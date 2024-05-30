#!/usr/bin/python3
""" pickle? IT'S PICKLE RIIICK"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):

        """ initialization"""

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):

        """ displaying attributes"""

        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Is Student: " + str(self.is_student))

    def serialize(self, filename):

        """ serializing"""

        diccionario = self.__dict__
        with open(filename, 'wb') as file:
            pickle.dump(diccionario, file)

    @classmethod
    def deserialize(cls, filename):

        """deserializing and saving"""

        with open(filename, 'rb') as file:
            saving = pickle.load(file)
        dummy = CustomObject(saving.name, saving.age, saving.is_student)
        return(dummy)
