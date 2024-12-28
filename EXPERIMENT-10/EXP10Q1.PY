#Write a program to display a/b where a and b are integers. 
# If b=0, display infinite by handling the ZeroDivisionError


def divide(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is: {result}")
    except ZeroDivisionError:
        print("Infinite (division by zero is not allowed)")

# Test cases
divide(10, 2)  # Expected output: 5.0
divide(10, 0)  # Expected output: Infinite
