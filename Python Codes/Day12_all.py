# Day 12 of 50 Days of Python 
# Tuesday, 23-11-2021
'''

1. Reading from files 
2. Writing to Files
3. Examples (Wrt files)
4. Functions
5. Function Arguments
6. Examples (Wrt Functions)
7. Assignment
'''


''' ########## TEXT FILES #########
#Eg. 1: Reading text files
#line =  [line.strip() for line in open('eg1.txt')]
# Try this# line2 = open('eg1.txt').read()

#Eg. 2: Writing to files
f1 = open('writefile.txt', 'w')
print('Okay,  I know nothing about it.', file=f1)
print('And I mean the same thing.', file=f1)
f1.close()
line =  [line.strip() for line in open('writefile.txt')]


#Eg. 3: Let's say you have results of NBA Players viz
#11/23/2021, Robert Morris, 61, Mount St. Mary's, 63

lines = [line.strip() for line in open('scores.txt')]
games = [line.split(',') for line in lines]
print(max([abs(int(g[2])-int(g[4])) for g in games]))

lines = [line.strip() for line in open('scores.txt')]
games = [line.split(',') for line in lines]

biggest_diff = 0
for g in games:
    diff = abs(int(g[2])-int(g[4]))
    if diff>biggest_diff:
        biggest_diff = diff
        game_info = g
print(game_info)
print(diff)'''

##### WORDPLAY ########
#Eg4: Print all 3 letters
'''
wordlist = [line.strip() for line in open('wordlist2.txt')]
for word in wordlist:
    if len(word)==3:
        print(word)'''

#try print([word for word in wordlist if len(word)==6])
'''
wordlist = [line.strip() for line in open('wordlist2.txt')]
#Eg 5: Starts with ac vs AC or da vs DA
for word in wordlist:
    if word[:2]=='ac' or word[:2]=='da':
        print(word)

wordlist = [line.strip() for line in open('wordlist2.txt')]
#Eg 5: Starts with ac and ends with tor #actuator
for word in wordlist:
    if word[:2]=='ac' or word[:3]=='tor':
        print(word)'''


#Eg 6: Determine what %age starts with a vowel
def calci():
    wordlist = [line.strip() for line in open('wordlist2.txt')]
    count = 0
    for word in wordlist:
        if word[0] in 'aeiou':
            count=count+1

    print(100*count/len(wordlist))
calci()
