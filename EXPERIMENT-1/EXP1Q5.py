# A) WAP to swap numeric values of two variables
#	i) With using third variable
#	ii) Without using third variable
#   B) WAP to swap string values of two variables
#	i) With using third variable
#	ii) Without using third variable

a=10
b=5
temp=a
b= temp
print("a=",a)
print("b=",b)


a=10
b=5
a,b=b,a
print("a=",a)
print("b=",b)


a="HELLO"
b="WORLD"
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)


a="WORLD"
b="HELLO"
a,b=b,a
print("a=",a)
print("b=",b)