# Write a Python program using try-except block with a suitable example.

try:
    x = int(input())
    y = int(input())
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero.")