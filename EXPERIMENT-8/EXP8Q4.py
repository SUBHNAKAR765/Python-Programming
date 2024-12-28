# WAP in python to read an entire text file.

def read_file(file):
    with open(file, 'r') as f:
        text = f.read()
    print(text)

read_file('planets.txt')
