
num = int(input("Enter a number: "))

n = num
sum_armstrong = 0
while n > 0:
    digit = n % 10
    sum_armstrong += digit ** 3
    n //= 10

#ARMSTRONG NUMBER
if sum_armstrong == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

#PERFECT NUMBER 
sum_factors = 0
for i in range(1, num):
    if num % i == 0:
        sum_factors += i

if sum_factors == num:
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")


#ADAM NUMBER 
original_num = num
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

if original_num == reverse_num:
    square_original = original_num ** 2
    square_reverse = reverse_num ** 2
    reverse_square_original = 0
    while square_original > 0:
        digit = square_original % 10
        reverse_square_original = reverse_square_original * 10 + digit
        square_original //= 10

    if reverse_square_original == square_reverse:
        print(original_num, "is an Adam number")
    else:
        print(original_num, "is not an Adam number")

    print(original_num, "is a Palindrome number")
else:
    print(original_num, "is not a Palindrome number")
