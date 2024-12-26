# Write a Python program using try-except-else block with a suitable example.

try:
    x = int(input())
    y = int(input())
    result = x / y
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Result:", result)