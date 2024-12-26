# wap in python code to design an arithmatic calculator (+-*/%,<<,>>) with inputting 2 numbers.


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

op = input("Enter an operation (+, -, *, /, %, <<, >>): ")

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b
elif op == '%':
    result = a % b
elif op == '<<':
    result = a << b
elif op == '>>':
    result = a >> b
else:
    result = "Invalid operation"

print(f"The result is: {result}")
