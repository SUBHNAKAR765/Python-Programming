# Write a Python program using try-except-else-finally block with a suitable example.

try:
    x = int(input())
    y = int(input())
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result is:", result)
finally:
    print("Execution complete.")