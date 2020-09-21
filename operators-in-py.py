#!/bin/python 

# this program shows the different operators in python

"""
some operators shown here are 
exponentiation operator : **
floor division operator : //

logical opertors  like "and" "or" "not"
identity operators like : "is" and "is not"
membership operators like : "in" and "not in"

bitwise opearators like : & | ^ ~ << >>

"""

fruits = {"apple","banana","guava","litchi"}
if "apple" in fruits:
    print("yes apple is a fruit")

else:
    print("No it is not a fruit")


if 5 == 10 or 4 == 4:
    print("Atleast one of them is true")

x = 2
x **= 3
print(x)

y = 5
y = y // 2
print(y)

a = 10    #0000 1010
b = 1     #0000 0001
c = a&b   # a AND b   """ the and gate returns 1 if both the bits are 1
print(c)  #expected result is zero
d = a | b # a OR b    or gate returns 1 if any of the bits is 1
print(d)  # expected result is 0000 1011  that is 11


