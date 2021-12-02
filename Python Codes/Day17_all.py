'''
Day 17 of 50 Days of Python Programming

1. Errors and Exceptions
    Syntax Error
    Exceptions
2. Handling Exceptions

'''

'''#1. use of except clause
def anAttempt():
    x= int(input("Please enter a number: "))
    x/0

try:
    anAttempt()
except ZeroDivisionError as err:
    print("Handling run-time errors: ", err)'''

#Eg 2:
try:
    raise Exception('Hello', 'World')

except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)    # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
    
  #Subclasses
    x,y = inst.args #unpack instances ie Tuple Unpacking
    print('x =', x)
    print('y =', y)