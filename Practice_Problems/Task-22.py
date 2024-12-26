#  Write a Python program to illustrate the use of __init__ method with a suitable example.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

p = Person("John", 25)
p.display()