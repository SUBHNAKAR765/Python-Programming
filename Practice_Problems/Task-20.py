#Write a Python program using class and object to input two numbers by input() member function 
# to calculate sum and display in display() function

class Calculator:
    def input_numbers(self):
        self.a = int(input())
        self.b = int(input())

    def display(self):
        print(self.a + self.b)

obj = Calculator()
obj.input_numbers()
obj.display()
