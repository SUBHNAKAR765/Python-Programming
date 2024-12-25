str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = ""
i = 0

while i < min(len(str1), len(str2)):
    result += str1[i] + str2[i]
    i += 1

result += str1[i:] + str2[i:]

print("Interleaved string:", result)