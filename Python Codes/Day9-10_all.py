# Day 9-10 of 50 Days of Python 
# Sunday,21-11-2021
'''
Recall: List vs Sequences 
1. Tuples
2. Sets
3. Dictionary
4. Be involved!! 
'''
'''
#TUPLES ()
fruits = ("Apples", "Mangoes", "Almonds")
numbers = (1,2,4,6,7,8)
boolean = (True, False, False, "true")
print(fruits)
print(numbers)
print(boolean)


fruits = ("Apples", "Mangoes", "Almonds",1,2,4,6,7,8,
True, False, False, "true")

#What is a constructor
#tuple()
fruit = tuple(("1 Apples", "2 Mangoes", "3 Almonds"))

print (fruit)

# How do we change Tuple Values
fruit = ("Apples", "Mangoes", "Almonds")
print(fruit)
fruit1 = list(fruit) 
fruit1.remove("Apples")
fruit = tuple(fruit1)
print(fruit)

#Solution 1)Convert to a list
            #2)Add the new item

        #3) Finally convert back to tuple

#Q: Can we add a tuple to a tuple?
fruit = ("Apples", "Mangoes", "Almonds")
cost = (56, 78, 100)
#added = fruit + cost
fruit+=cost #Same as fruit = fruit+cost
print(fruit)


#WHAT IS TUPLE UNPACKING?
fruit = ("Apples", "Mangoes", "Almonds")
# Unpacking
(he, hi, nay) = fruit
print(he)
print(hi)
print(nay)


#Why use asterisk *
fruit = ("Apples", "Mangoes", "Almonds")
# Example
(he, *hi) = fruit
print(he)
print(hi)


#Printing / Looping through Tuple
fruit = ("Apples", "Mangoes", "Almonds")
for item in fruit:
    print(item)
'''
##########################################
    #INTRO to SETS: Used to store many items in a single variable
#How do I create a set? 
fruits = {"Apples", "Mangoes", "Almonds"}
print(fruits)


#Assignmnet
# Can you create a game playing character, based on what you've learnt so far?






