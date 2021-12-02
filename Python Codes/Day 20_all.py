'''
Day 20 of 50 Days of Python Programming

REGULAR EXPRESSIONS - Missing Notes

1. The search() Function
2. The split() Function
3. The sub() Function
4. The Match Object
5. The string() Function

GUI Programming using Tkinter

1. Basics of a GUI Program
2. Tkinter Widgets
3. Widget Classes
4. Geometry Management
5. Tkinter Button
6. Themed Widgets
7. Tkinter Labels
'''
############## REGULAR EXPRESSIONS-CONTD ##########
'''#Eg 1: The search() Function
import re
txt = "It is raining in Nigeria now"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

#Eg 2:  With no Match, "None" is returned
import re
txt = "Indians are very friendly prople"
x = re.search("Jovial", txt)
print(x)

#Eg 3: The split() Function
import re
txt = "Welcome to the heritage city, Mysore"
x = re.split("\s", txt)
print(x)

#Eg 4: Split() with maxsplit parameter
import re
txt = "The silicon valley of India"
x = re.split("\s", txt, 9) #Explain behaviour using 0,3,4,7 and none
print(x)

#Eg 5: The sub() Function
import re
txt = "The city that never sleeps"
x = re.sub("\s", "*", txt)
print(x)

#Eg 6: The sub() Function using count parameter
import re
txt = "The city that never sleeps"
x = re.sub("\s", "*", txt, 6)
print(x)

#Eg 7: Using the Match Object
import re
txt = "The city that never sleeps"
x = re.search("e", txt)
print(x)#Returns an object

#Eg 8: Using span() to search for words that starts with upper case
import re
txt = "The Scotland of India is Shillong"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Eg 9: Use of print and string()
import re
txt = "The Scotland of India"
x = re.search(r"\bS\w+", txt)
print(x.string)
'''


########## Tkinter #########

'''#Eg 1: Hello World Tkinter Program
from tkinter import * 
from tkinter.ttk import *

root = Tk() #Root-Main window object

root.title("My First Program")# First progra Title

label = Label(root, text ="Hello World !").pack()# What output will be shown

root.mainloop() #The mainloop() used to run the app

#################################################
#Eg 2: Use of Widgets and Geometry Management
from tkinter import *

root = Tk()#Create the root window

root.title("My Second Program")# First progra Title

frame = Frame(root) #Frame, contained root window

frame.pack() # One of geometry methods

button = Button(frame, text ='Welcome Home!')# button inside frame which isinside root
button.pack()

root.mainloop() #Tkinter event loop

#####################################
#Eg 3: Creating a tkinter button

from tkinter import * ## imports everything from tkinter module

root = Tk()# Creates the tkinter window

root.geometry('350x150')# Opens a window with dimension 150x150

btn = Button(root, text = 'Click to Disappear!', bd = '5',command = root.destroy) #Creates a Button

btn.pack(side = 'top') # Positions the button at the top of the window.

root.mainloop() # The main loop

#########################################
#Eg 4: Button without tk themed widget

from tkinter import *

# The imported tkinter.ttk module will automatically
# override all the widgets present in tkinter module.
from tkinter.ttk import *

root = Tk() # Creates an Object

# Initialize tkinter window with dimensions 150x150
root.geometry('350x150')

btn = Button(root, text = 'Click Now!',command = root.destroy)

# Set the position of button on the top of window
btn.pack(side = 'bottom')

root.mainloop()
'''
############################
#Eg 5: Tkinter Label
from tkinter import *
#from tkinter.ttk import *

top = Tk()
top.geometry("500x400")
#The label for Username
user_name = Label(top,text = "Username").place(x = 40,y = 60)

#Password label
user_password = Label(top,text = "Password").place(x = 40,y = 100)

submit_button = Button(top,text = "Submit").place(x = 40,y = 130)

user_name_input_area = Entry(top,width = 30).place(x = 110,y = 60)

user_password_entry_area = Entry(top,width = 30).place(x = 110,y = 100)

top.mainloop()


