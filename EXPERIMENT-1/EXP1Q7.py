# Enter a paragraph and display the sub-string by using string slicing.

paragraph = input("Enter a paragraph: ")
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
substring = paragraph[start:end]
print("Sub-string:", substring)
