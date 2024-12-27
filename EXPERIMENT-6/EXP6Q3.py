# Execute an arithmetic calculator using function.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation == '+':
        print(add(x, y))
    elif operation == '-':
        print(subtract(x, y))
    elif operation == '*':
        print(multiply(x, y))
    elif operation == '/':
        if y != 0:
            print(divide(x, y))
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")

calculator()