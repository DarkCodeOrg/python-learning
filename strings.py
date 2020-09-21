""" demonstrating the use of arrays len upper lower strip split replace and slicing in python """

string_old = "  Hello, World!!  "

string = string_old.strip()


print(len(string))

for i in range(len(string)):
    print(string[i])

print(string[0:5])

print(string.upper())
print(string.lower())
print(string.replace("H","F"))


"""
below is the demonstration of string check , cocatenation , format
"""

a = "First"
b = "Second"
age = 30

c = a + b  #cocatenation of string
d = a + "" + b
print(c)
print(d)


x = "Fir" in a  #check string using in
print(x)

y = "Sec" not in b  #check string using not in 
print(y)


txt = "i am anonymous and my age is {}"
print(txt.format(age))

"""Escape characters"""

print("Hi this is \"Mr Anonymous\" nice to see you ;-) <3 4 U")




