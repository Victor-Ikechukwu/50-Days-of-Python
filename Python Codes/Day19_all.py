'''
Day 19 of 50 Days of Python Programming

PYTHON REGULAR EXPRESSIONS

1. Finding Patterns with Regular Expressions (RE)
2. Regular Expression Matching: A Review
3. Matching Multiple Groups with the pipe (|) Character
4. Matching with the Question Mark (?)
5. Matching Zero or more characters (*)
6. Matching One or More characters (+)
7. Matching Specific Repetitions with Curly Brackets{}
8. Character Classes
'''
############## REGULAR EXPRESSIONS ##########
'''#Eg 1: An Intro: Without RE
def isPhoneNumber(text):
    if len(text) != 12:
        return False       # 234-806-3219 vs 91-78234-42190
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

#print('234-806-4190 is a valid phone number:')
#print(isPhoneNumber('61-806-4219'))
#print('Is my name a valid phone number?')
#print(isPhoneNumber('Victor-Victor'))
#####TRY THIS CODE ########
msg = 'Call me on my personal number 234-556-1234 tomorrow. Or on 34-806-4219 my office number.'
for i in range(len(msg)):
    found = msg[i:i+12]
    if isPhoneNumber(found):
        print('Phone number is valid: ' + found)
print('Done')

#Eg 2: Finding patterns with RE
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mn =  phoneNumRegex.search('My number is 234-777-4205.')
print('Phone number found: ' + mn.group())

mn1 =  phoneNumRegex.search('My number is 34-777-4205.')


#Eg 3: Grouping with Parenthesis
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mn =  phoneNumRegex.search('My number is 234-777-4205.')
print(mn.group(0))
print(mn.group(2))

areaCode, mainNum = mn.groups() #Explain group vs groups()
print(areaCode)
print(mainNum)

#Eg 4: Matching Multiple Groups with "|" character
import re

heroRegex = re.compile (r'Bahuballi|Prabhas')
mn = heroRegex.search('Bahuballi and Prabhas.')
print(mn.group())

mn1 = heroRegex.search('Prabhas and Bahuballi')
print(mn1.group())

#Eg 5: Matching Multiple characters
import re
baRegex = re.compile(r'Ba(huballi|ratnagar|tilmore|tholomew)')
mn = baRegex.search('Bahuballi is my favourite Bollywood movie')
print(mn.group(2))
#print(mn.group(1))

#Eg 6:Optional Matching with the Question Mark
import re
batRegex = re.compile(r'Bat(wo)?man')
bt = batRegex.search('The Adventures of Batman begins')
print(bt.group())

bt1 = batRegex.search('The Adventures of Batwoman, haha')
print(bt1.group())

#Eg 7: Matching Zero or More with the Star
import re
batRegex = re.compile(r'Bat(wo)?man')
bt = batRegex.search('The Adventures of Batman begins')
print(bt.group())

bt1 = batRegex.search('The Adventures of Batman begins, PART 2')
print(bt1.group())

bt2 = batRegex.search('The Adventures of Batwoman, haha')
print(bt2.group())

bt3 = batRegex.search('The Adventures of Batwoman, part 2')
print(bt3.group())

#Eg 8: Matching One or More with the Plus (+)
import re

bat = re.compile(r'Bat(wo)+man')
bt = bat.search('The Adventures of Batman begins')
#print(bt.group())

bt1 = bat.search('The Adventures of Batmanmanbat begins, PART 2')
print(bt1.group())

bt2 = bat.search('The Adventures of Batwoman, haha')
bt2 == None
print(bt2.group())

#Eg 9: Matching Specific Repetitions with Curly Brackets
import re

hiRegex = re.compile(r'(Hi){3}')
h1 = hiRegex.search('HiHiHi')
print(h1.group())

h2 = hiRegex.search('Hi')
#h2 == None
print(h2)
'''
########## CHRISTMAS SONG using Character Classes #####
import re
masRegex = re.compile(r'\d+\s\w+')
print(masRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
