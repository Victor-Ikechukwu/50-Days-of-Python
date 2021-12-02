'''
Day 17-18 of 50 Days of Python Programming

PYTHON EXCEPTION HANDLING

1. Errors vs Exceptions 
2. Catching Exceptions using Try and Except
3. Catching Specific Exceptions
4. Try & Else Clause
5. Finally Keyword in Python
6. Raising Exceptions
'''


'''# Eg 1: Simple Runtime Error
a = [2, 5, 7]
try:
    print ("The second element with format specifier = %d" %(a[1]))
    print ("The second element  = ", a[1])
    # Throws error since there are only 3 elements in array
    print ("The sixth element = %d" %(a[5]))
 
except:
    print ("Oops!, An error occurred")

#Eg 2: Handling Multiple Errors with one except stmt
def haha(a):
    if a < 5:
         # throws ZeroDivisionError for a = 4
        b = a/(a-4)
 
    # throws NameError if a >= 5
    print("Value of b is = ", b)
     
try:
    haha(4)
    haha(6)
# NB: Braces () are necessary here for multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and are Handled")
except UnboundLocalError:
    print("UnboundLocalError Occurred and are Handled")

#Eg 3: Program to depict else clause with try-except
def tryThis(a,b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b results in 0")
    else:
        print (c)
 
# Driver program to test above function
tryThis(6.0, 3.0)
tryThis(4.0, 4.0)

#Eg 4: Finally Keyword in Python Demo
# No exception Exception raised in try block
try:
    m = 7//0  # raises divide by zero exception.
    print(m)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Hey!, You can't divide by zero")
 
finally:
    # This block is always executed
    # regardless of exception rules.
    print('This is always executed')

#Eg 5: Raising an Exception

try:
    raise NameError("Hey, who are you?")  # Raise Error
except NameError:
    print ("I am just an exception bro!")
    raise  # To determine whether the exception was raised or not'''



'''def pattern(n):
    num = 65
    for i in range (0,n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end='')
        num=num+1
        print('\r')
    
n=5
pattern(n)'''

'''
############## REGULAR EXPRESSIONS ##########
#Eg 1:
def isPhoneNumber(text):
    if len(text) != 12:
        return False       # 234-806-3219
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True

print('234-806-4190 is a valid phone number:')
print(isPhoneNumber('234-806-4219'))
print('Is my name a valid phone number?')
print(isPhoneNumber('Victor-Victor'))'''