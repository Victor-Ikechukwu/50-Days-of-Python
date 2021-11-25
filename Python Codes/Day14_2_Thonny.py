'''
1. What is Python Recursion
2. 

'''

'''#Eg. 1: Example of a recursive function
def factorial(x):
    """This is a recursive function
    to find the factorial of a number"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 5
print("The factorial of", num, "is", factorial(num))

#Eg. 2: Testing the maximum depth of Recursion
def recurse():
    recurse()
recurse()

#Eg. 3: Another case of max recursion exceeded
def function():
    x = 10
    function()

#Eg. 4: Checking Recursion Limit
from sys import getrecursionlimit
getrecursionlimit()


#Eg. 5: You can change it, too, with setrecursionlimit():
from sys import getrecursionlimit,setrecursionlimit
setrecursionlimit(2000)
getrecursionlimit()

#Eg. 6: Count down program
def countdown(n):
    print(n)
    if n == 0:
        return             # Terminates recursion
    else:
        countdown(n - 1)   # Recursive call
        
print(countdown(5))

#Eg. 7: Some more concise ways
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)
# Or using non-recursive ways for comparison
def countdown(n):
    while n >= 0:
         print(n)
         n -= 1
countdown(5)

#Eg. 8: Calculate Factorial of a number

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

factorial(10)

#Eg 9: Use print() to make it readable
def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

print(factorial(4))


#Eg. 10: Recursion using For loop
def factorial(n):
     return_value = 1
     for i in range(2, n + 1):
        return_value *= i
     return return_value

factorial(5)

#Eg. 11: Recursion using reduce & lambda functions
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])

factorial(4)

######### Speed / Execution Time Comparison ######
#Eg 12:
from timeit import timeit
print(timeit("print(string)", setup="string='Hello'", number=100))

#Eg 13: Using Recursive Call
setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
    """

from timeit import timeit
print(timeit("factorial(4)", setup=setup_string, number=100))'''

#Eg 13: Using Iterative Implementation
setup_string = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
        """
from timeit import timeit
print(timeit("factorial(4)", setup=setup_string, number=1000))

'''
#Eg 14: Hey, factorial is available in math module
from math import factorial
print(factorial(6))'''
