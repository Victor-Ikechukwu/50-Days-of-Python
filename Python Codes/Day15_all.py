'''
1. Object Oriented Programming
        Creating your own classes
        Inheritance
2. Mini Projects
3. Homework
'''

#Eg 1. A Simple Class
'''class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b

e = Example(10, 14)
print(" The Sum is ", e.add())

#Eg 2. A Real Example
from string import punctuation

class SanityCheck:# Pre -processing over
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c,'')
        s = s.lower()
        self.words = s.split()
    
    def number_of_words(self):
         return len(self.words)
    
    def starts_with(self, s):
        return len([w for w in self.words if w[:len(s)]==s])

    def number_with_length(self, n):
        return len([w for w in self.words if len(w)==n])

st = 'This is a more practical example of OOP!'
sc = SanityCheck(st)
print(sc.words)
print('Number of words to Check: ', sc.number_of_words())
print('Number of words starting with "t":', sc.starts_with('t'))
print('Number of 4-letter words:', sc.number_with_length(4))

##########    INHERITANCE #########
#Eg. 3
class Parent:
    def __init__(self, a):
        self.a = a
    def method1(self):
        return self.a*3
    def method2(self):
        return self.a+'!!!'
    
class Child(Parent):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def method1(self):
        return self.a*9
    def method3(self):
        return self.a + self.b
    
p = Parent('Hey')
c = Child('Yes', 'Dad!')

print('Parent method 1: ', p.method1())
print('Parent method 2: ', p.method2())
print()
print('Child method 1: ', c.method1())
print('Child method 2: ', c.method2())
print('Child method 3: ', c.method3())

#Eg. Add some new methods to the Child class
class Parent:
    def __init__(self, a):
        self.a = a
    def method1(self):
        return self.a*3
    def method2(self):
        return self.a+'!!!'
    def print_var(self):
        print("The value of this class's variables are:")
        print(self.a)
    
class Child(Parent):
    def __init__(self, a, b):
        Parent.__init__(self, a)
        self.b = b
    def method1(self):
        return self.a*9
    def method3(self):
        return self.a + self.b
    
    def print_var(self):
        Parent.print_var(self)
        print(self.b)
   
p = Parent('Hey')
c = Child('Yeah', 'Bro')

print('Parent method 1: ', p.method1())
print('Parent method 2: ', p.method2())
print()
print('Child method 1: ', c.method1())
print('Child method 2: ', c.method2())
print('Child method 3: ', c.method3())

'''
# Eg 4: Playing Card Example
# A Tic-Tac-Toe Example
class tic_tac_toe:
    def __init__(self):
        self.B = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        self.player = 1
        
    def get_open_spots(self):
        return [[r,c] for r in range(3) for c in range(3)
            if self.B[r][c]==0]
    
    def is_valid_move(self,r,c):
        if 0<=r<=2 and 0<=c<=2 and self.B[r][c]==0:
            return True
        return False
    
    def make_move(self,r,c):
        if self.is_valid_move(r,c):
            self.B[r][c] = self.player
            self.player = (self.player+2)%2 + 1
            
    def check_for_winner(self):
        for c in range(3):
            if self.B[0][c]==self.B[1][c]==self.B[2][c]!=0:
                return self.B[0][c]
        for r in range(3):
            if self.B[r][0]==self.B[r][1]==self.B[r][2]!=0:
                return self.B[r][0]
        if self.B[0][0]==self.B[1][1]==self.B[2][2]!=0:
            return self.B[0][0]
        if self.B[2][0]==self.B[1][1]==self.B[0][2]!=0:
            return self.B[2][0]
        if self.get_open_spots()==[]:
            return 0
        return -1

#Print the Winner
def print_board():
    chars = ['-', 'X', 'O']
    for r in range(3):
        for c in range(3):
            print(chars[game.B[r][c]], end=' ')
        print()
        
game = tic_tac_toe()
while game.check_for_winner()==-1:
    print_board()
    r,c = eval(input('Enter spot, player ' + str(game.player) + ': '))
    game.make_move(r,c)
    
print_board()
x = game.check_for_winner()
if x==0:
    print("It's a draw.")
else:
    print('Player', x, 'wins!')
