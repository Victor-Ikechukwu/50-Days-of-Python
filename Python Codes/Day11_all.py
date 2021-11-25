# Day 11 of 50 Days of Python 
# Monday, 22-11-2021
'''

1. Sets-Contd...
2. Dictionary
3. Mini Exercise!!
4. Assignment
'''




#####################################################################3
    #INTRO to SETS: Used to store many items in a single variable
#How do I create a set? 
'''fruits = {"Apples", "Mangoes", "Almonds"}
print(fruits)
fruits.clear()
print(fruits)

# Using Union()
names = {"Anjali", "Amith","Ananya", "Renin"}
age ={19, 20, 18, 19}
#setBoth = names.union(age)
#print(setBoth)

#Uisng update()
names.update(age)
print(names)

## Use of intersection_update()
company1 = {"Facebook", "Apple", "Amazon"}
company2 = {"Amazon","Netflix", "Google"}
company1.intersection_update(company2)
print(company1)'''

 # DICTIONARY


##### Extended Example On Dictionary  #####
#A dictionary is a more general version of a
#list. Here is a list that contains the
#number of days in the months of the year:
#day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Here is a dictionary of the days in the months of the year:
#days = {'January':31, 'February':28, 'March':31, 'April':30,
#            'May':31, 'June':30, 'July':31, 'August':31,
#                'September':30, 'October':31, 'November':30, 'December':31}

'''
diwali = {"Ram" : "A Hindu God that has mysterious powers",
          "Sita" : "The Goddess of Himalayas",
          "Bahuballi": "The strongest God"}
word = input("Enter any word related to Diwali like Ram/Sita" )
print("The definition is: ", diwali[word])
'''

######### MINI EXERCISE   ############
# Can you count how frequent certain words appear in a text?

from string import punctuation

#i. read from file, remove caps and punctuation, and split into words
text = open('bahuballi.txt').read()

text = text.lower()
for p in punctuation:
    text = text.replace(p, '')
words = text.split()

#ii. build the dictionary of frequencies
d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1
        
#iii. print in alphabetical order
items = list(d.items())
items.sort()
for i in items:
    print(i)
    
#iv. print in order from least to most common
items = list(d.items())
items = [(i[1], i[0]) for i in items]
items.sort()
for i in items:
    print(i)

####### ASSIGNMENT ###########
For this problem, use the dictionary from
the beginning of this chapter whose keys are
month names and whose values are the number
of days in the corresponding months.

(a) Ask the user to enter a month name and use the dictionary to tell them how many days
are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month
(e) Modify the program from part (a) and the dictionary so that the user does not have to
know how to spell the month name exactly. That is, all they have to do is spell the first
three letters of the month name correctly.'''


'''
# Can we design a Scrabble Game
word = input("Enter a word")
points = {'A':1, 'K':8, 'X':8, 'Z':10}
score = sum([points[c] for c in word])
print(score)'''












