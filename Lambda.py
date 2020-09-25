# this program shows the usage of the lambda function in python
# the lambda function refers to any anonymous function 

# syntax :    
# lambda arguments : expression 

# wwhen to use lambda function :::: when u need an anonymous function for a short period of time or when u ned to pass an function as a argument to another function 


add = lambda a,b,c,d : a + b + c + d

print(add(1,2,3,4))

sub = lambda a,b : a - b

print(sub(10,11))
 
def myfunc(x):
    return lambda n: n*x

y = myfunc(20)
print(y(2))

say_hello = lambda : print("hello")

say_hello()


my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = list(filter(lambda x: x%2==0,my_list))   # the filter function takes two arguments one function and another list 


print(new_list)


