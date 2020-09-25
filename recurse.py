# program depicting the use of recursion in python 

def my_recursion(n):
    if n == 1:
        return 1
    else:
        return (n * my_recursion(n-1))

x = my_recursion(900)
print(x)

