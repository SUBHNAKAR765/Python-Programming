# A file contains a word "donkey" multiple times. 
# You need to write a program which replaces this word with $$$$$ by updating the same file.

def replace_word():
    try:
        with open("story.txt", "r") as file:
            content = file.read()
        content = content.replace("donkey", "$$$$$")
        with open("story.txt", "w") as file:
            file.write(content)
        print("Word replaced successfully.")
    except FileNotFoundError:
        print("The file 'story.txt' does not exist.")

replace_word()
