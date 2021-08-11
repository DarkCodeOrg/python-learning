from os import read

# file reading 
file = open('trial.txt' , 'r')

for each in file:
    print(each)

print (file.read())

# file writing 

file.write("this is the write function")
file.write("this lets us write to the file")
file.close   # the close function lets us close all the resources in use


## Append mode 

file = open('trial.txt','a')

file.write("writing this in append mode")
file.close
