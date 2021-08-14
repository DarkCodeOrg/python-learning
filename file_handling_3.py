### continued ...........
## File pointer    ( analogous to a bookmark in a book )

import sys
#sys.path.append("/home/david/hello_world/python/basics")
import os

#import list_adv as f_list  ## it has functions to manipulate a list

## infile = open("filename","r") would open the file and put the file
# pointer at the beginning of the file
# ch = infile.read(1) would read 1 byte (one character)  from the file
# str = infile.read(2) would read 2 bytes from the place where the
# file pointer left 

#############################################
###       WORKING WITH BINARY FILES       ###
#############################################

import pickle

# pickling / serialisation = converting an python object into a byte-stream 
# unpickling / deserialization = converting the byte stream again into python object
##  the pickle module has dump() and load() methods to write and read to and from a file
# Creating / opening / closing binary files
#  

dfile = open("student_new.dat","rb+")  # b specifies to open it in binary mode
data_w = {}  ## creating an empty dictionary for writing purpose
data_r = {}  ## creating an empty dictionary for reading purpose
 ## reading the file 
try :
    print("file student_new.dat conains the following records :")
    while True:         ## sets to false if end of file is encountered
        data_r = pickle.load(dfile)
        print(data_r)
except EOFError:
    dfile.close()

dfile = open("student_new.dat","ab+")
No_of_stdnt = int(input("enter the no of students in class :"))
for i in range(No_of_stdnt):
    name = input("Enter the name of the student :")
    roll = int(input("enter the roll no of the student :"))
    marks = int(input("eneter the marks obtained by the student :"))
    data_w['Name'] = name
    data_w[ 'Roll'] = roll
    data_w[ 'Marks'] = marks
    ## thedata_r  above three lines fillup the dictionary
    pickle.dump(data_w,dfile)

dfile.close()


## searching in a binary file

found = False
dfile = open("student_new.dat","rb")
search_for = []  ## these are the roll nos to find for
reply = 'y' 
while reply == 'y':
    foo = int(input("Enter the roll number to search for :"))
    search_for.append(foo)
    reply = input("Do you wish to search for more ?(y/n) :")
else :

    try:
        print("Searching in the file student_new.dat ......")
        while True:
            data_r = pickle.load(dfile)
            if data_r['Roll'] in search_for:
                print(data_r)
                found = True
    except EOFError:
        if found == False:
            print("no such records found..")

        else:
            print("search successful")

            dfile.close()


