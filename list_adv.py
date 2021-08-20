"""  this program shows the use of list : adding item, removing item, printing it (iterating), clearing it """

import sys

thisislist = ["apple","banana"]
print("this is the initial list ",thisislist)
print("this is the length of the list ",len(thisislist))

def Additem():
    item = str(input("Enter the name of the element that you want to add = "))
    thisislist.append(item)
    print(thisislist)
    menu()
def RemItem():
    item = str(input("Enter the name of the element that you want to remove = "))
    thisislist.remove(item)
    print(thisislist)
    menu()
def PrintList():
    for x in thisislist:
        print(x)
    menu()
def CheckList():
    search = str(input("Enter the item u wanna search: "))
    if search in thisislist:
        print("Yes it is present")
    else:
        print("It is not present")
    print(thisislist)
    menu()

def AddItemPos():
    item = str(input("Enter the item u want to Add : "))
    pos = int(input("Enter the position Where u wanna add the item : "))
    thisislist.insert(pos,item)
    print(thisislist)
    menu()

def ClearList():
    thisislist.clear()
    print(thisislist)
    menu()

def menu():
    print('''
    0) Quit
    1) Add an element to the list
    2) Add an item at a particular position
    3) Remove an element from the list
    4) Display the list
    5) Check if an item exists
    6) Clear the list 
          ''')
    selection = int(input("What do you want to do: "))
    if selection == 0:
        sys.exit()    
    elif selection == 1:
        Additem()
    elif selection == 2:
        AddItemPos()
    elif selection == 3:
        RemItem()
    elif selection == 4:
        PrintList()
    elif selection == 5:
        CheckList()
    elif selection == 6:
        ClearList()
    else:
        print("Invalid input")

menu()


### to use this as a module in other programs uncomment all the 
### lines with menu()

