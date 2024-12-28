# WAP in python to count frequency of characters in a file

def count_char_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()

    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    for char, freq in frequency.items():
        print(f"'{char}' : {freq}")

# Usage
count_char_frequency('planets.txt')
