# continued......

file_1 = open('trial.txt',"r")
s = file_1.readlines() # the readlines function reads the entire contents of the file into a list (here s)

print(s)
file_1.close

## displaying the size and no of lines of a file 
file_2 = open("trial.txt","r")
foo = file_2.read()
size = len(foo)
linecount = len(file_2.readlines())
print("size of the given file is ")
print(size, "bytes")
print("no of lines is ", linecount)
file_2.close()

## creating a file and holding data in it

filenew = open("student.dat" , "w")
No_of_stdnt = int(input("enter the no of students in class :"))
for i in range(No_of_stdnt):
    name = input("Enter the name of the studnet :")
    roll = int(input("enter the roll no of the student :"))
    Marks = int(input("eneter the marks obtained by the student :"))
    data = str(roll) + "," + name + "," + str(Marks) + '\n'
    filenew.write(data)

    filenew.flush()  ## the flush functions use us defined below

filenew.close()

## reading the no of consonants and vowels from a file

file1 = open("trial.txt","r") 
ch = ""
Vcount = 0
Ccount = 0
for ch in file1.read():
    if ch in set("AEIOUaeiou"):
        Vcount +=  1
    elif ch in set("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"):
        Ccount += 1

print("Vowels in the file",Vcount)
print("Consonants in the file",Ccount)

file1.close()


## the Flush function
# the flush function is used to write data still pending in the buffer
# the flush function is implicitly called by the close() function
# but can also be called explicitly to force write the data
# 


# use of strip , rstrip , lstrip 
## strip() = removes the character from both ends
# lstrip() = removes the character from the left end
# rstrip() = removes the character from the right end

myfile = open("stripping.txt",'r+')
text = myfile.read()
text_stripped = text.lstrip('.,asd')
print(text_stripped)

myfile.close()


