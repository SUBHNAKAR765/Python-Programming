# 1st program 
Name ="SubhakarSahoo"
Age= 15
CGPA =8.73
print(Name) 
print (Age )
print(CGPA )

print (type(Name))
print (type(Age))
print (type (CGPA))

                                    #OPERATOR#

#ARITHMETIC OPERATOR 
a=5
b=5
print (a+b)
print(a-b)
print (a*b)
print (a/b)
print (a%b)
print (a**b)

#RELATIONAL / COMAPARISION  OPERATOR 
a=10
b=15
print (a==b)
print (a!=b)
print (a>b)
print (a<b)
print (a<=b)
print (a>=b)

#ASSIGNMENT OPERATOR 
a=10 
a=+20
a-=10
a*=10
a/=10 
print (a)
print(a)
print (a)

#LOGICAL OPERATOR 
a=10
b=15
print(not(a>=b))
print (a>b and b<a)
print (a>=b or a<=b )



                                              #TYPE  CASTING
                                            
a = 3.15
a = str(a)
print (type (a))

a=5
b= float("5")
print(a+b)
print (type(a+b))

                                             #INPUT IN PYTHON 
# name =input("enter your name ")
# print ('my name is :', name )

value = float (input("ENTER THE VALUE :"))
print (value )
print (type(value))




                                                #PROBLEMS 
# Q1)PRINT YOUR NAME , AGE, MARKS BY TAKING INPUT FROM THE USER 
Name =input ("ENTER YOUR NAME : ")
Age =int (input ("ENTER YOUR AGE :"))
Marks = float (input ("ENTER YOUR MARKS :"))
print (Name )
print (Age )
print (Marks )

#Q2) WAP TO INPUT TWO NUMBERS  AND PRINT THEIR SUM 
a= int(input ("ENTER THE FIRST NUMBER : "))
b= int(input ('ENTER THE SECOND NUMBER :') )
sum= a+b
print (type (a+b),sum)

#Q3) WAP TO INPUT SIDE OF A SQUARE AND PRINT ITS AREA 
s =int(input("ENTER THE SIDE OF THE SQUARE :"))
area =s*s
print (area )

#Q4) WAP TO INPUT TWO NUMBERS AND PRINT THEIR AVERAGE 
a=int (input("ENTER THE FIRST NUMBER :"))
b=int (input("ENTER THE SECOND NUMBER :"))
average = int ((a+b)/2)
print (average)
print(type (average ))

#Q5) WAP TO TAKE 2 NUMBERS AS INPUT AND PRINT IF A IS GREATER OR EQUAL TO B . IF NOT PRINT FALSE 
a= int (input ("ENTER THE 1ST NUMBER: "))
b= int (input ("ENTER THE 2ND NUMBER: "))
print  (a<=b)

#Q6) Loop to print even numbers from 1 to N
N=5
for i in range(1, N + 1):
    if i % 2 == 0:  # Check if the number is even
        print(i)
