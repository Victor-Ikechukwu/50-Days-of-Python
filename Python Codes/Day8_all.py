# Day 8 of 50 Days of Python 
# Thursday, 19-11-2021
'''
LISTS
1. Assignment Revision
2. Git vs GitHub Tutorial
3. Joins (Opposite of Split)
3. List Comprehension
4. Two-Dimensional lists
5. Demo (Examples)
6. Assignments!! 
'''

'''
#Can we use a list to store multiple items/ contain multiple data types? Yes or No
#Answer:
ls = ['Car',1, 9.250, "Bike", 2, 400000, 'Cycle',1,15000.260, True]
print(ls)

data = [["first_Name", "long names", 1, 2, 3, 4],
        ["last_Name", "long names", 5, 6, 7, 8]]
print(data)
#data[0]
#data[0][0]

#### JOINS ####
#Eg 1.
ls = ['Agu', 'gha', 'si']
print(''.join(ls))#Joins together into a sigle word
print(' '.join(ls))#with spaces
print(','.join(ls))
print('+++'.join(ls))

#Eg 2: Anagram word generator
from random import shuffle
word = input('Enter a word: ')

letter_list = list(word)
shuffle(letter_list)
anaya = ''.join(letter_list)
print(anaya)

#### LIST COMPREHENSION ####
#Eg 3
li = [i for i in range(11)]
print(li)

#Eg 4.
string = 'Hello'
L = [1,14,5,9,12]
M = ['one', 'two', 'three', 'four', 'five', 'six']
print([i**3 for i in range(1,8)]) 
#print([i*10 for i in L])
#print([c*2 for c in string])
#print([m[0] for m in M])
#print([i for i in L if i<10])
#print([m[0] for m in M if len(m)==3])

#### 2D Lists ####
L = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
for r in range(3):
    for c in range(4):
        print(L[r][c], end=" ")
    print() #Try explaining what happens here

#Another way
from pprint import pprint
pprint(L)

# Eg 3: Create two larger list using list comprehension
L = [[1]*50 for i in range(100)]
print(L)


######  MAJOR ASSIGNMENT   ################
# A program to play a simple quiz game. #
num_right = 0
# Question 1
print('What is the capital of India?', end=' ')
guess = input()
if guess.lower()=='new delhi':
    print('Correct!')
    num_right+=1
else:
    print('Wrong. The answer is New Delhi.')
print('You have', num_right, 'out of 1 right')

#Question 2
print('Which state has only one neighbour?', end=' ')
guess = input()
if guess.lower()=='karnataka':
    print('Correct!')
    num_right+=1
else:
    print('Wrong. The answer Karnataka.')
print('You have', num_right, 'out of 2 right,')
'''
#### 6) Game Simplified with list and loops #####
questions = ['What is the capital of India?',
'Which state has only one neighbour?']
answers = ['New Delhi','Karnataka']
num_right = 0
for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower()==answers[i].lower():
        print('Correct')
        num_right=num_right+1
    else:
        print('Wrong. The answer is', answers[i])
print('You have', num_right, 'out of', i+1, 'right.')

