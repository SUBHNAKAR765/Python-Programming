# WAP in  python  to find the average of maximum and minimum element of a list.

numbers = input("ENTER THE ELEMENTS IN THE LIST : ").split()
max_num = int(numbers[0])
min_num = int(numbers[0])
for num in numbers:
    if int(num) > max_num:
        max_num = int(num)
    if int(num) < min_num:
        min_num = int(num)
average = (max_num + min_num) / 2

print ("Maximum number :",max_num )
print ("Minimum number :",min_num )
print("The average of maximum and minimum element of a list : " , average)
