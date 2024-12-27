# [Output of this programme will be the value of K, L and P for each iteration of function foo until
#  the condition is true]
# Foo (n, P)
# K=n%10 n=n/10 P= P+K+n

n = 3042
P = 0
while n != 0:
    K = n % 10
    n = n // 10
    P = P + K + n
    print(K, n, P)