from os import read
import os

### checkout python docs for more https://docs.python.org/3/library/filesys.html
### file = open('filename' , 'mode')
""" 
 modes = r (read only)
         r+ (read and write)
         w (write)  ## the W mode overwrites the entire file.....so beware 
         a (append)  ## append mode appends text at the end of file
         x (create)
         t (text)
         b (binary)
"""

# file reading 
file = open('trial.txt' , 'r+')

for each in file:
    print(each)

print (file.read())

# file writing 

file.write("this is the write function\n")
file.write("this lets us write to the file\n")
file.close   # the close function lets us close all the resources in use


## Append mode 

file = open('trial.txt','a')

file.write("writing this in append mode\n")
file.close

## using write with with()

with open('trial.txt','r+') as file:
    text = file.read()
    file.write("writing from within with()\n")

## creating a file using x mode

file2 = open('newfile','x') ## creates the file ...returns error if the file already exists
os.remove("newfile")   ## this removes the file

## readline()

file3 =  open('trial.txt')
print(file3.readline())
print(file3.readline())    ## this would print the first two lines of the file

## create a file , add a line and a string , read them , split the string and store it in a list , delete the file by checking if it exists atfirst

file4 = open("myfile","x")
file4 = open("myfile","r+")
file4.write("this is the line\n")
file4.write("apple , banana , cherry , mango")
content = file4.read()
print(content)  #TODO debug here...

if os.path.exists("myfile"):
    os.remove("myfile")
else:
    print("the file doesnt exist\n")
