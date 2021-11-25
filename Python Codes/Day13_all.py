# Day 13 of 50 Days of Python 
# Wednesday, 24-11-2021

'''
1. Functions
        Creating & Calling
2. Function Arguments vs Parameters
        Arbitrary Arguments
3. The Pass Statement
4. Recursion
5. Lambda Function
6. Examples (Wrt Lambda Functions)
7. Assignment
'''
#1. Creating a Function

#2. Calling a Function

'''
#3. Arguments
def my_func(fname):
    print(fname + ",is my Friend")

my_func("Dhanush")
my_func("Mahesh")
my_func("Varsha")

#4. Parameters vs Arguments
def my_func2(fname, lname):
    print(fname + " " + lname)

my_func2("Akash", "Mahesh")

#5. Arbitrary Arguments, *args
def my_dish(*food):
  print("My favourite dish is " + food[1])

my_dish("Masala poori", "Biryani", "Idli")

#6. Keyword Arguments (using key = value pair)
def my_dish(f3,f2,f1):
  print("My favourite dish is " + f2)

my_dish(f1="Masala poori", f2="Biryani", f3="Idli")

#7. Arbitrary Keyword Arguments, **kwargs
def my_dish(**food):
  print("My favourite dish is " + food["f1"])

my_dish(f1="Masala poori", f2="Biryani", f3="Idli")

#8. Default Parameter Value
def my_country(country = "Nigeria"):
    print("I am from " +country)

my_country("Jamaica")
my_country("India")
my_country()
my_country("South Africa")

#9. Passing sequences as an argument
def my_function(fruits):
    for x in fruits:
        print(x)
fruits = ["Apples", "Bananas", "Mangoes"]
my_function(fruits)

#10. Can we return values


#11. Use of Pass Statement
def myPassStmt():
    pass

########  LAMBDA FUNCTIONS ##########

#12. Use of Lambda Expessions
ex = lambda a : a + 10
print(ex(15))

#13. Using two arguments
x = lambda a, b : a * b
print(x(4, 5))'''

#14. Using lambda to double a number
def myfunc(n):
    return lambda a : a * n
my_double = myfunc(2)
print(my_double(11))






