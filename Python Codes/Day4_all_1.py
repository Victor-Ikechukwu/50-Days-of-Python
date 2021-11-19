#Eg: With the use of elif stmt
# Emphasis on debugging the code and writing meaningful apps

name = input("Enter your name ")
age = int(input("How old are you?" ))
if name == 'Victor' and age==22:
    print("Welcome back, ", name)
elif age <=20:
    print("Hey, you joker!, you ain't Victor")
elif age > 100 and age < 130:
    print("I guess you must be a granny, haha")
elif age > 200:
    print("On a lighter note, you ain't suppose to be alive")
    
else:
    print("Please be serious!, Enter valid details...Thanks")