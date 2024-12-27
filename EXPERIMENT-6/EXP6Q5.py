# Wite a programme in python to check a user inputted string is palindrome or not by using function.

def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
