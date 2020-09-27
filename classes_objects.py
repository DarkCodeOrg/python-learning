#this program is an implementation of the classes and objects in python 

# classes serve as an blueprint for making objects in an code
# everything in OOP is regarded as an object 
# the properies defined in the class are called attributes and the functions are called methods


class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print("Hello I am " + self.name)

    def say_hi(self):
        print("HI EVERYBODY !!")

    

    
Human1 = Human("David",32,"male")

print(Human1.name)
print(Human1.age)
print(Human1.gender)
Human1.greet()
Human1.say_hi()

