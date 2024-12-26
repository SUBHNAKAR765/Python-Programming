#WAP to find all the prime number between 11 to 100. And print their sum.

sum_primes = 0
for num in range(11, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        sum_primes += num

print("Sum of primes:", sum_primes)
