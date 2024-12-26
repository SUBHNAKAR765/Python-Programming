amount = int(input("Enter the amount to withdraw: "))

if amount % 100 != 0:
    print("Invalid amount. Please enter an amount that is a multiple of 100.")
else:
    n2000 = amount // 2000
    amount = amount % 2000
    
    n500 = amount // 500
    amount = amount % 500
    
    n200 = amount // 200
    amount = amount % 200
    
    n100 = amount // 100

    result = "Please take "

    if n2000 > 0:
        result += f"{n2000} note{'s' if n2000 > 1 else ''} of 2000 Rupees, "
    if n500 > 0:
        result += f"{n500} note{'s' if n500 > 1 else ''} of 500 Rupees, "
    if n200 > 0:
        result += f"{n200} note{'s' if n200 > 1 else ''} of 200 Rupees, "
    if n100 > 0:
        result += f"{n100} note{'s' if n100 > 1 else ''} of 100 Rupees"

    print(result.rstrip(", "))
