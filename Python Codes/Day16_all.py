'''
Day 16 of 50 Days of Python Programming

1. Classes - contd
2. Scopes and Namespaces in Python
3. Class Definition and Objects
4. Instance of a class
5. Method Objects
6. Python Iterators
7. Generators
8. Generator Expressions
10. Homework
'''

'''#Eg 1: Use of Scopes and Namespaces in Python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

#Eg 2: A Simple Class Object
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

#Step 2: Create an isntance of the class
x = MyClass()
#x1 = MyClass() # How many instances can be created?
#Step 3: Call using the class instance
print(x.i)
print(x.f())
#x.f()


#Eg. 3: A more Complex Example
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex()
print(x.r, x.i)


#Eg 4: Class and Instance Variables
class Cat:
    
    kind = 'Feline'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Cat('Persian')
e = Cat('Bengal')

e.kind                  # shared by all Cats
d.kind                  # shared by all Cats

d.name                  # unique to d
e.name                  # unique to e


#Eg 5: A tricky Example
class Cat:
    tricks = []             # mistaken use of a class variable
    
    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Cat('Siamese')
e = Cat('Persian')
d.add_trick('Roll over :)')
e.add_trick('Play dead :(')
d.tricks                # unexpectedly shared by all cats


#Eg 6: Correct Design of the class: Use an instance variable
class Cat:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each instance of cat

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Cat('Persian')
e = Cat('Saimese')

d.add_trick('Roll over')
e.add_trick('Play dead')

d.tricks
e.tricks


#Eg 7: Priority over the instance example

class StdGrade:
        purpose = 'Grading System'
        sem = ' ,for 7th Semester'
        
h1 = StdGrade()    
#print(h1.purpose, h1.sem)
#Try re-assigning sem and see what happens
h2 = StdGrade()
h2.sem = 'For 8th semester'
#print(h1.purpose, h1.sem)
print(h1.purpose, h2.sem)


#Eg. 8: Odds & Ends Examples
class Emp:
    pass

magi = Emp()  # Create an empty Employee record

#Fill the fields of the record
magi.name = 'Amar Magi'
magi.dept = 'CSE'
magi.salary = 1000000


#Eg 9: Notes on Iterators
for element in [1, 2, 3]:
    print(element)
    #print("End of list")
for elem in (1, 2, 3):
    print(elem)
    #print("End of Tuple")
for key in {'one':1, 'two':2}:
    print(key)
    #print("End of Dict")
for char in "123":
    print(char)
    #print("End of Char")
for line in open("myfile.txt"):
    print(line, end='')
#try s =  abc example

#Eg 10: Add iterator() to a class
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('Hemanth')
iter(rev)

for char in rev:
    print(char)
'''
#Eg. 11: Generators: more compact but less versatile
#generator definitions and tend to be more memory friendly than equivalent list comprehensions.
    
print(sum(i*i for i in range(4))) #Sum of Squares
xv = [1, 1, 1]
yv = [4, 8, 10]
print(sum(x*y for x,y in zip(xv, yv))) #Zip = dot product

data = "Welcome"
print(list(data[i] for i in range(len(data)-1, -1, -1)))#String converted to a list and then used generators
