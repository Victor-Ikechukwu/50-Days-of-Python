"""
Day 6 of 50 Days to the new year (2022) challenge
Thursday-17/11/2021

********* OUTLINE ***********
1) Some While Examples
2) Use of sys.exit()
3) Strings (Concatenation and Repetition)
4) Slicing
5) Assignments
Next Class: Read up Functions
"""

#1. Use of While Loop    
name = ''
while not name: #aka TRUTH vs FALSE Values
    print('Enter your first name:?') 
    name = input()
print('How many guests will be visiting?')
numOfGuests = int(input())
if numOfGuests: 
    print('Be sure to have enough room for all your guests.')
print('Done')


#2. Use of sys.exit()
import sys
while True:
     print('Type exit to quit.')
     response = input()
     if response == 'exit':
         sys.exit()
print("You've entered ", response + '.') 




         
 
