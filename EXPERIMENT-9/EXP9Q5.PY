# Write a python program to rename a file to
#"renamed_by_python.txt".

import os

def rename_file():
    try:
        os.rename("planets.txt", "renamed_by_python.txt")
        print("File renamed successfully.")
    except FileNotFoundError:
        print("The file 'planets.txt' does not exist.")

rename_file()
