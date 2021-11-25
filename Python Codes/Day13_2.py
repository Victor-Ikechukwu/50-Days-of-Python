'''def my_func(fname):
    print(fname + ",is my Friend")
    
my_func("Samarth")
my_func("Amar")
my_func("Anjali")
my_func("Deeksha")
my_func("Niharika")


def my_func(fname):
    print("Wecome " +fname + ",is my Friend")
    
my_func("Samarth")
my_func("Amar")
my_func("Anjali")
my_func("Deeksha")
my_func("Niharika")


def my_func2(fname, lname):
    print(fname + " " + lname)

my_func2("Akash", "Mahesh")
my_func2("Ananya", "Prakash")
my_func2("Anjali", "Hemanth")
#5. Arbitrary Arguments, *args
def my_dish(*food):
  print("My favourite dish is " + food[1])

my_dish("Masala poori", "Biryani", "Idli")

#6. Keyword Arguments (using key = value pair)
def my_dish(f3,f2,f1):
  print("My favourite dish is " + f3)

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
#my_country()
my_country("South Africa")
my_country()

#9. Passing sequences as an argument
def my_function(fruits):
    for x in fruits:
        print(x)
fruits = ["Apples", "Bananas", "Mangoes"]
my_function(fruits)

#10. Can we return values
def multiply(x):
    return 10 * x

print(multiply(1))
print(multiply(11))
print(multiply(111))
print(multiply(1111))
print(multiply(11111))
print(multiply(111111))

def myfunc():
    pass

#12. Use of Lambda Expessions
ex = lambda a : a + 10
print(ex(15))

#13. Using two arguments
x = lambda a, b : a % b
print(x(5, 4))'''

def myfunc(n):
    return lambda a : a * n
my_double = myfunc(2)
my_tripple = myfunc(3)
my_fourth = myfunc(4)

print(my_double(11))
print(my_tripple(11))
print(my_fourth(11))
















