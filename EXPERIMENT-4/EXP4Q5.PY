#WAP to input a lowercase string from user and convert it into upper case without using inbuilt function.  

lower_str = input("Enter a lowercase string: ")
upper_str = ""
for char in lower_str:
    if 'a' <= char <= 'z':
        upper_str += chr(ord(char) - 32)
    else:
        upper_str += char

print("Uppercase string:", upper_str)
