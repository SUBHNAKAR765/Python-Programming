number = input("Enter a 6-digit number: ")


sum1 = 0
for i in range(6):
        digit = int(number[i])
        sum1 += digit ** (i + 1)

reversed_number = number[::-1]

sum2 = 0

for i in range(6):
        digit = int(reversed_number[i])
        sum2 += digit ** (i + 1)

difference = sum1 - sum2

print("Difference (Sum1 - Sum2):", difference)