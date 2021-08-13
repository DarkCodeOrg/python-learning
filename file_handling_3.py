### continued ...........
## File pointer    ( analogous to a bookmark in a book )

import sys
import os

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

dfile = open("student_new.dat","ab")  # b specifies to open it in binary mode
data = {}  ## creating an empty dictionary
No_of_stdnt = int(input("enter the no of students in class :"))
for i in range(No_of_stdnt):
    name = input("Enter the name of the student :")
    roll = int(input("enter the roll no of the student :"))
    marks = int(input("eneter the marks obtained by the student :"))
    data['Name'] = name
    data['Roll'] = roll
    data['Marks'] = marks
    ## the above three lines fillup the dictionary
    pickle.dump(data,dfile)

dfile.close()




