from abc import ABC, abstractmethod


class Animal():

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return ("Bark")


class Cat(Animal):

    def sound(self):
        return ("Meow")
