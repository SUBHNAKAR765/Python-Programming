# Write a program in python to demonstrate Try,
#  Except with Finally block. What is the need of finally block in python explain this.

def show_finally():
    try:
        res = 10 / 2
        print("Result is:", res)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    finally:
        print("Finally block executed")

    try:
        res = 10 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError")
    finally:
        print("Finally block executed")

show_finally()
