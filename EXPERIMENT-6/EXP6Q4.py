#Write a python programme to do the addition and multiplication of numbers 
# inputted from user in the form of tuple (use function).



def add(numbers):
    return sum(numbers)

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

user_input = input("Enter numbers separated by commas (e.g., 1,2,3): ")
numbers = tuple(map(int, user_input.split(',')))

addition_result = add(numbers)
multiplication_result = multiply(numbers)

print(f"Addition of numbers: {addition_result}")
print(f"Multiplication of numbers: {multiplication_result}")
