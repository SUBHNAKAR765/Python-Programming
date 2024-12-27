# WAP  in  python to count positive number, negative number and zeros in a list.

numbers = input( "ENTER THE NUMBERS : ").split()
positives = 0
negatives = 0
zeros = 0
for num in numbers:
    if int(num) > 0:
        positives += 1
    elif int(num) < 0:
        negatives += 1
    else:
        zeros += 1
print("positive:" , positives )
print("negative :" , negatives  )
print("zero:" , zeros  )