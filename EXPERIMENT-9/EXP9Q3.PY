# Write a program to make a copy of a text file "Galaxy.txt”.
#[Galaxy.txt contains minimum 25 galaxies name those are discover by NASA Hubble space telescope].

def copy_file():
    try:
        with open("Galaxy.txt", "r") as file:
            content = file.read()
        with open("Galaxy_copy.txt", "w") as copy:
            copy.write(content)
        print("File copied successfully.")
    except FileNotFoundError:
        print("The file 'Galaxy.txt' does not exist.")

copy_file()
