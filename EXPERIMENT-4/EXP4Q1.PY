amount = float(input("Enter the amount: "))

if amount <= 5000:
    discount = amount * 0.05
elif amount <= 15000:
    discount = amount * 0.12
elif amount <= 25000:
    discount = amount * 0.20
else:
    discount = amount * 0.30

print("Amount:", amount)
print("Discount:", discount)
