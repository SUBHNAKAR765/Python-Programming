#WAP to enter two number from user input and find their LCM and HCF.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y:
    x, y = y, x % y
hcf = x

lcm = (a * b) // hcf

print("HCF:", hcf)
print("LCM:", lcm)
