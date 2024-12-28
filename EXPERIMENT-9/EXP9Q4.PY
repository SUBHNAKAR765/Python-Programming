# Write a program to wipe out the contents of a file using python. 
# [Create that text file named as planets.txt that contains list of planets in the solar system].

def wipe_file():
    try:
        with open("planets.txt", "w") as file:
            file.write("")
        print("Contents of the file have been wiped.")
    except FileNotFoundError:
        print("The file 'planets.txt' does not exist.")

wipe_file()
