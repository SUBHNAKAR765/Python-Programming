# Write a python program to open three files planets1.txt, 
# planets2.txt and planets3.txt. If any of these files are not present, 
# a message without exiting the program must be printed promoting the same.
 
 
def open_files():
    filenames = ["planets1.txt", "planets2.txt", "planets3.txt"]
    for name in filenames:
        try:
            with open(name, "r") as file:
                print(f"{name} opened successfully")
        except FileNotFoundError:
            print(f"{name} not found.")

open_files()

