# Write a program to read the text from a given file "poems.txt" and find out whether it contains the words "twinkle" and "star". 
# First create a text file that contains the poem "twinkle twinkle little star".

def check_words():
    try:
        with open("poems.txt", "r") as file:
            text = file.read()
            if "twinkle" in text and "star" in text:
                print("The file contains both 'twinkle' and 'star'")
            else:
                print("The file does not contain both words")
    except FileNotFoundError:
        print("The file 'poems.txt' does not exist.")

check_words()
