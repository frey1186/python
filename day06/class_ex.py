class Animal(object):
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):

    @staticmethod
    def talk(self):
        return 'Woof! Woof!'

animals = [Cat('Missy'),
           Dog('Dassie')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())