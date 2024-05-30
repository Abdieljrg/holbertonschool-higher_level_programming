#!/usr/bin/python3
""" pickle? IT'S PICKLE RIIICK"""
import pickle


class CustomObject:
    def __init__ (self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display (self):
        print ("Name: " + self.name)
        print ("Age: " + str(self.age))
        print ("Is Student: " + str(self.is_student))

    def serialize(self, filename):
        diccionario = self.__dict__
        with open (filename, 'w') as file:
            pickle.dump (diccionario, file)

    @classmethod
    def deserialize(cls, filename):
        with open (filename, 'r') as file:
            saving = pickle.load(file)
        dummy = CustomObject(saving.name, saving.age, saving.is_student)
        return (dummy)