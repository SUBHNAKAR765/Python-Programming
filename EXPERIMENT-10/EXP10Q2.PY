# Write a program in python to demonstrate different types of Exceptions and Errors. 

def show_exceptions():
    try:
        a = [1, 2, 3]
        print(a[3])
    except IndexError:
        print("IndexError")

    try:
        d = {"a": 1}
        print(d["b"])
    except KeyError:
        print("KeyError")

    try:
        n = int("abc")
    except ValueError:
        print("ValueError")

    try:
        res = "text" + 5
    except TypeError:
        print("TypeError")

    try:
        with open("file.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("FileNotFoundError")

show_exceptions()
