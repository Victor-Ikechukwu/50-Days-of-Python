# Day 7 of 50 Days of Python 
# Thursday, 18-11-2021
'''
LISTS
1. Random module in list
2. Splits
3. List methods
4. Making copies & changing lists
5. Demo (Examples)
6. Be involved!! 
'''

'''
#################### EASY EXAMPLES ########################
# 1) WAP that generates a list L of 20 random numbers between 1 and 100.
from random import randint
L = []
for i in range(20):
    L.append(randint(1,100))
print(L)

# 2) Replace each element in a list L with its square.
L = [1,2,4,5,6,7,8,9]
for i in range(len(L)):
    L[i] = L[i]**2
print(L)

# 3)  Count how many items in a list L are greater
#than 20.
from random import randint
L = []
count = 0
for item in range(30):
    L.append(randint(1,100))
    if item>20:
        count=count+1
print(count)

# 4) WAP that prints out the two largest
#and two smallest elements of a list called scores.
scores = [23, 67, 98, 12, 10, 3, 19, 78, 55, 63, 90]
scores.sort()
print('Two smallest: ', scores[0], scores[1])
print('Two largest: ', scores[-1], scores[-2])


################### EXTENDED EXAMPLES #############
#Eg 5:  We can use choice to pick a name from a list of names.
from random import choice
names = ['Adithya', 'Sneha', 'Shusma', 'Pradnya']
current_player = choice(names)
print(current_player)


#Eg 6:
from random import sample
names = ['Syed', 'Safeer', 'Ahmad', 'Jabeen']
team = sample(names, 2)
print(team)

#Eg 7:
from random import choice
s='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
for i in range(1000):#be warned...start with very small numbers
    print(choice(s), end='')

#Eg 8:
from random import shuffle
players = ['Henry', 'Bob', 'Alice', 'Victor']
shuffle(players)
for i in players:
    print(i, 'it is your turn.')

# SPLITS #Eg 9
ik = 'Hi! I am called Iyke naa:)'
print(ik.split())

# Eg 10: Count how many times certain words occur in a string
from string import punctuation
def demo1():
    stg = input('Enter a long sentense?')
    for c in punctuation:
        s = stg.replace(c, '')
    s = stg.lower()
    L = stg.split()

    word = input('Enter a word: ')
    print(word, 'appears', L.count(word), 'times.')
demo1()

#Eg 11: Good for splitting mobile nos
ms = '+234-806-419-4290'
print(ms.split('-'))




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














''''

==========================================
                        HOME WORK 
1. Write a program that generates a list of 30 random numbers between 1 and 100 inclussive.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list
(f) Print how many odd numbers are in the list
'''




