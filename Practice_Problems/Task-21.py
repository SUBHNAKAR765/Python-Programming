# Write a Python program to illustrate the use of class and 
# object to pass by value to the function and calculate the sum and display.

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display_sum(self):
        print(self.a + self.b)

obj = Calc(3, 4)
obj.display_sum()
