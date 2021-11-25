# Day 14 of 50 Days of Python 
# Thursday, 25-11-2021

'''
1. Recursion
2. Functions - Mini Projects 
3. Exception Handling
4. Assignment
'''
'''
#1. Checking Recursion Limit
def countdown(n):
    print(n)

    if n==0:
        return
    else:
        countdown(n-1)
countdown(5)'''
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



