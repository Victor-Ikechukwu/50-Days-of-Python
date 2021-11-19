"""
Day 4 of 50 Days to the new year (2022) challenge
Monday-15/11/2021

********* OUTLINE ***********
1) Magic  Variables & Methods in Python
2) Operators:
    i)Comparative and Boolean (Truth Tables)
2) Flow Control:
    i)Conditions and Code Blocks 
3) While Loop:
    irritating and infinite loops
"""

'''
#Example 1
#>>>dir(int)
num1 = 10
num2= num1+20
#print(num2)
num2.__add__(20)


#Example 2
n1= 22
str(n1)
#int.__str__(n1)

#Example 3
num1 = 23.067
num2 = -12.156
num3 = num1 * num2
float(num3)
print(num3)

#flow control examples
#Eg 1:
name = input("Enter your name ")
if name == 'Victor':#victor vs VICTOR
    print('Welcome back, ', name)


#Eg 2: Modified version
name = input("Enter your name ")
if name == 'Victor':
    print('Welcome back, ', name)
else:
    print("Hello, Mr./Mrs ", name)
'''
#Eg: With the use of elif stmt
name = input('What\'s your name')
age = int(input("How old are you?" ))
if name == 'Victor' and age==22:
    print("Welcome back, ", name)
elif age <=30:
    print("Hey, you joker!, you ain't Victor")
elif age > 100 and age < 130:
    print("I guess you must be a granny, haha")
elif age > 200:
    print("On a lighter note, you ain't suppose to be alive")
    
else:
    print("Please be serious!, Enter valid details...Thanks")

'''
################## WHILE LOOPS ############
num = 0 #Using IF stmts
if num < 5:
    print('Hello, Bro!!')
    num = num + 1

num1 = 0 # Using FOR LOOP
while num1 < 5:
    print('Hello, world.')
    num1 = num1 + 1
  
# An irritating while loop
name = ''
name = "What\'s your name"
while name != 'Victor':
    print('Please type your name.')
    name = input()
print('Thank you!')

#Modified version, an application of name guess program
while True:
    name = input('Please enter your name?')
    if name == 'Victor':
        break
print('Thank you bro!')#Try indenting this..haha


# Infinite loop in python

i  = 0
while (i < 10):
    print(i)

while True:
    print("Hello")
'''

    

