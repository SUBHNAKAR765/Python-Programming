# Write a programme in python using function to execute the given tree 
# by displaying the values of statements present in the level 
# and whenever the value of n is equals to 0 the function will get exit 
# and return 0(call the function foo with the value (3042,0) 
# and foo will call itself by the updated value of n and p).


def foo(p, n):
    if n == 0:
        return 0
    print(f"p: {p}, n: {n}")
    p = p // 2
    n -= 1
    return foo(p, n)

foo(3042, 3)  
