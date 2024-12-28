# WAP in python to count the number of characters, words and lines in a file.

def count_file_content(filename):
    with open(filename, 'r') as file:
        text = file.read()

    lines = text.splitlines()  # Splits by lines
    words = text.split()  # Splits by whitespace
    characters = len(text)

    print(f"Number of characters: {characters}")
    print(f"Number of words: {len(words)}")
    print(f"Number of lines: {len(lines)}")

# Usage
count_file_content('planets.txt')
