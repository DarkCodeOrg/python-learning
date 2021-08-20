#this program is an implementation of the classes and objects in python 

# classes serve as an blueprint for making objects in an code
# everything in OOP is regarded as an object 
# the properies defined in the class are called attributes and the functions are called methods





class Human:
    def __init__(self,name,age,gender):  ## the init function is executed whenever a class is initiated   // we can use this function to pass parameters to the object when it is created  
                                         ## this func is also called a constructor
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):   ## self refers to the name of the object that is being creatd using this class 
        print("Hello I am " + self.name)

    
        print("HI EVERYBODY !!")
    
    
class Robot:
    def introduce_self(self):
        print("my name is ",self.name)  ## 
        print("my weight is " ,self.weight)
        print("my address is ", self.addr)

class Animal:
    def __init__(self):
        self.name = input("enter the name of the animal :")
        self.age = int(input("enter the age of the animal :"))
        self.habitat = input("enter the habitat of this animal :")
        self.owner = input("enter the name of owner :")
        self.care_taker_robo = r1

    def info(self):
        print("I am a ",self.name)
        print("my age is ",self.age)
        print("my owner is :",self.owner)

H1 = Human("David",32,"male")
print(H1.name)
print(H1.age)
print(H1.gender)
H1.greet()



r1 = Robot()
r1.name = "ROBO1"
r1.weight = 30
r1.addr = "USA"
r1.introduce_self()



a1 = Animal()
a1.info()
a1.care_taker_robo.introduce_self()

