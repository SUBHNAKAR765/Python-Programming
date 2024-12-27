# WAP in python to find the odd numbers and even numbers from entered list and display them in two list.

numbers = [int(x) for x in input("Enter the numbers : ").split()]
even_numbers = []
odd_numbers =  []
for nu in numbers:
    if nu % 2 == 0:
        even_numbers.append(nu)
    else:
        odd_numbers.append(nu)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)



