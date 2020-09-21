#/bin/python 

""" this program depicts the use of sets in python """

# sets are unordered and unindexed they are written using curly braces {}
# we cannot change items but we can add items and remove items

myset = {"maths","physics","chemistry","Computer Science"}
print(myset)  # set is printed in opposite fashion 

for x in myset:
    print(x)

print("banana" in myset)
print("maths" in myset)

myset.add("Subjects")
print(myset)

# adding multiple items using update method

myset.update(["update","multiple","items"])
print(myset)

print(len(myset))

myset.remove("update")  # remove takes exactly one argument 
print(myset)

myset.clear()
print(myset)

""" joining two sets """

set1 = {"Facebook","Apple","Amazon"}
set2 = {"Netflix","Google"}

print("set1 is ",set1,"set2 is ",set2)

set3 = set1.union(set2)
print(set3)

# set constructor

thisisset = set(("new","set"))
print(thisisset)
