## updating in a binary file
# 
# tell() and seek() 
#
import pickle
from sys import flags

infile = open("trial.txt",'r')

print("initially the file_pointer is at = ",infile.tell())
print("reading 4 bytes : ",infile.read(4))
print("now the file pointer is art :",infile.tell())

## the tell function gives the current position of the file pointer
print("now printing results of the seek function")

infile.seek(10) ## default mode , puts the file pointer to the 
                 # 10th byte from the beginning

infile.seek(5,1) ## mode 1 , puts the file pointer to the 5th byte(forward direction) from
                  # the current file pointer position

infile.seek(-10,2) ## mode 2 , puts the file pointer to the 10th byte backward from the 
                    # end of file

#######################################################################
####    UPDATING THE RECORDS OF A FILE AT A PARTICULAR POSITION     ###
#######################################################################

## read the file student_new.dat and give 10 marks bonus to students who have scored more that 550
## 

upfile = open("student_new.dat","rb+")
stu = {}    ## crating a empty file to store the records in the file
found = False

try:
    while True:
        rpos = upfile.tell()
        stu = pickle.load(upfile)

        if stu['Marks'] > 550:
            stu['Marks'] += 10
            upfile.seek(rpos)
            pickle.dump(stu,upfile)
            found = True

except EOFError:
    if found == False:
        print("no such records found")
    else:
        print("record(s) have been updated")

    upfile.close()

