""" this program is for the demonstration of tuples in python """
""" this also demonstrates convertig tuples to a list, check if tuple exists and so on.... """


mytuple = ("hello","hi","tuple","bye")
# tuples ar immutable that is they cannot be modified no adding of items no removing of items 
# it is like a static list

for x in mytuple:
    print(x)

""" workaround for adding items to a tuple """
y = list(mytuple)
y.append("workaround")
mytuple = tuple(y)

for x in mytuple:
    print(x)

# creating tuple with  a single element
newtuple = ("new",) # we have to insert that comma otherwise python would not understand it as a tuple

print(newtuple)

