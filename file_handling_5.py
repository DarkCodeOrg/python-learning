## CSV file manipulation

import csv
 

infile = open("student.csv","ra+",newline='\n')
infile_1 = open("student.csv","ra+",newline='')

## writing to csv files
## delimeter refers to the separator used in a csv file to separate datas

##  we have to create a writer object at first   ..... csv.writer(input-file) creates the writer object
## the writer object is required for coverting user entered data into
## delimited strings 
## the writer object has many methods like writerow, writerows
## etc....
data_writer  = csv.writer(infile_1)
data_writer.writerow(['Rollno','Name','Marks'])  ## the coloumn headings are written here
                                                ## the above line writes a row with Rollno,Name,Marks  written ....that serves as a heading

no_of_students = int(input("Enter the no of students :"))

for i in range(no_of_students):
    print("Student record ",i+1)
    rollno = int(input("Enter the roll number of the student :"))
    name = input("Enter the name of the student :")
    marks = int(input("Enter the marks obtained by the student :"))
    student_record = [rollno,name,marks]
    data_writer.writerow(student_record)


## 

infile.close()
infile_1.close()




