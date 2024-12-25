#WAP to enter your name and print after deleting first and last characters of the name.

name = input("Enter your name: ")
if len(name) > 2:
    result = name[1:-1]
else:
    result = ""
print("Name after deleting first and last characters:", result)