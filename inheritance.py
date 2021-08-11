# the child class is the one that has all the properties of the base class and might have some extra features

class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age

    def printname(self):
        print("name is ",self.name,"age is",self.age)

Y = Person("david",30)
Y.printname()

class Student(Person):
    def __init__(self,name,age,year):     ## this init function overrides the parents __init__ function 
        super().__init__(name,age)   ## the super function helps in inheriting the variables and their related properties from the base/parent class 
        self.graduationyear = year
   
    def printyear(self):
        print("graduation year is : ",self.graduationyear)

X = Student("DAVE",16,2020)
X.printname()
X.printyear()