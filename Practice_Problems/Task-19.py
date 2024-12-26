# Write a Python program using a variable-length argument function with an example
def total(*nums):
    return sum(nums)

print(total(1, 2, 3))  # Output: 6
print(total(5, 10))  # Output: 15
