'''
******* OUTLINE ********
1) Nested-IF
2) Pass Statement
3) Switch Case in Python
4) FOR Loop
5) The Loop Variable
6) The range function
7) Homework:Write a program that prints a giant letter A.
Allow the user to specify how large the letter should be.

'''

# Eg 1: Use of nested-if
'''
Syntax
The syntax of the nested if...elif...else construct may be −

if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   elif expression4:
      statement(s)
   else:
      statement(s)
else:
   statement(s)

#A nested if statement is an if statement placed inside another if statement. Nested if
#statements are often used when you must test acombination of conditions before deciding on the proper action.
#num1 = 150 #Try & modify this
num1 = int(input("Enter any integer number"))
if num1 < 250:
   print ("What you entered is less than 250")
   if num1 == 170:
      print ("You entered 170")
   elif num1 == 120:
      print ("You entered 120")
   elif num1 == 70:
      print ("You entered 70")
   elif num1 < 50:
      print ("The value you entered is less than 50")
else:
   print ("Cannot find a true expression")

print ("Bye!")


# Eg 2: Accept a number from the user and
#check if the number is +ve, 0, or -ve
num = float(input("Enter any number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("It's a Positive number")
else:
    print("It's a Negative number")
'''

#Eg 3:

'''It is used when the statement is required
syntactically, but you do not want
that code to execute. The pass statement
is the null operation; nothing happens when
it runs. The pass statement is also useful
in scenarios where your code will
eventually go but has not been entirely
written yet'''
'''
a = 63
b = 27
if(a<b):
    pass
#else:
    #print("b is less than a")

# Eg: Pass in a list
li =['a', 'b', 'c', 'd']
 
for i in li:
    if(i =='a'):
        pass
    else:
        print(i)
'''

########## SWITCH CASE IN PYTHON ##########
'''
A switch case statement in a computer programming language is a powerful tool
that gives the total programmer control over the program’s flow according to
an expression’s outcomes or a variable.

Switch cases are mainly used to execute a different block of codes in relation
to the results of expression during the program run time.


#Eg 1: Switch using an if-else-if ladder...No need to use Functions
#def switch():
option = int(input("Enter your option to get the month : "))

if option == 1:
    result = "January"
    print("The month is = ",result)
 
elif option == 2:
    result =  "Febuary"
    print("The month is = ", result)
 
elif option == 3:
    result = "March"
    print("The month is = ", result)
elif option == 4:
    result =  "April"
    print("The month is = ", result)
 
elif option == 5:
    result = "May"
    print("The month is = ", result)
elif option == 6:
    result =  "June"
    print("The month is = ", result)
 
elif option == 7:
    result = "July"
    print("The month is = ", result)
 
else:
    print("Invalid!, Enter numbers b/w 1-12") 
#switch()

#Executes perfectly without a function
option = int(input("Enter your option from 1-12 to get the month : "))

if option == 1:
    result = "January"
    print("The month is = ",result)
 
elif option == 2:
    result =  "Febuary"
    print("The month is = ", result)
 
elif option == 3:
    result = "March"
    print("The month is = ", result)
elif option == 4:
    result =  "April"
    print("The month is = ", result)
 
elif option == 5:
    result = "May"
    print("The month is = ", result)
elif option == 6:
    result =  "June"
    print("The month is = ", result)
 
elif option == 7:
    result = "July"
    print("The month is = ", result)
 
else:
    print("Invalid!, Enter numbers b/w 1-12")
 
#Eg 2:Switch case statement using class to convert literal to string ‘month’
class SwitchCaseDemo:
 
    def switch(self, month):
        default = "Incorrect month"
        return getattr(self, 'case_' + str(month), lambda: default)()
 
    def case_1(self):
        return "January"
 
    def case_2(self):
        return "February"
 
    def case_3(self):
        return "March"
 
    def case_4(self):
        return "April"
 
    def case_5(self):
        return "May"
 
    def case_6(self):
        return "June"
    def case_7(self):
        return "July"
    def case_8(self):
        return "August"
    def case_9(self):
        return "September"
    def case_10(self):
        return "October"
    def case_11(self):
        return "November"
    def case_12(self):
        return "December"
 
s = SwitchCaseDemo()
print(s.switch(3))
print(s.switch(4))
print(s.switch(10))


#Example 3 – Using a dictionary mapping to return value
num ={
'a' : 200,
'b' : 223,
'c' : 224,
'd' : 225
}
inp = input('Enter  a character : ')
print('The result is : ', num.get(inp, 7))# the 7 is the default value if there are no keys that match 
'''
#IN SUMMARY: Python does not have an in-built switch-case construct, but you can use
#dictionary mapping instead of the switch case.
#Python developer did not include the switch-case construct for a good reason.
#Although many programmers and developers have been pushing for the inclusion of switch case constructs in Python, whether their proposal will be considered, Python switch case alternatives serve even better.
'''
####### INTRODUCTION TO LOOPS #######

#Eg 1:
for i in range(7):
    print('Hello, World')
 
#Eg 2:
for i in range(3):
    num = eval(input('Enter any number: '))
    print ('The cubic value of your number is', num*num*num)
print('Haha, the loop is now over.')

#Eg 3:
print('Apple')
print('Banana')
for i in range(3):#Prints both thrice
    print('Carrots')
    print('Dragonfruit')
print('Eggplant')

# Eg 4:
print('A')
print('B')
for i in range(3):
    print('C')
for i in range(3):
    print('D')
print('E')
'''

##### The Loop Variable, Explain the Behaviour

#for i in range(1,7):
    #print(i)

#How about ...
#for i in range(3):
 #  print(i+1, '** Hello')

###### THE RANGE FUNCTION #######
#range(2,15,3)prints 2,5,8,11,14
#range(9,2,-1)prints 9,8,7,6,5,4,3


# Let's send Falcon to space..haha...Try to delay it 
'''
import time
for i in range(5,0,-1):
    time.sleep(5)
    print(i, end=' ')
print('Blasting off into SPACE!!!')


#What's the Output?
#for i in range(4):
#    print('*'*6)
  
for i in range(4):
    print('* '*(i+1))


'''
# Program that Prints large letter A
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);

