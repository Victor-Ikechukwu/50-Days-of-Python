'''#Day5_p1.py
grade = int(input('Enter students score: '))
if grade>=90:#90 ...100
    print('A')
if grade>=80 and grade<90:
    print('B')
if grade>=70 and grade<80:
    print('C')
if grade>=60 and grade<70:
    print('D')
if grade>=50 and grade<60:
    print('E')
if grade<50:
    print('F')
'''

# How about the modified version
grade = eval(input('Enter your score: '))
if grade>=90:
    print('A')
elif grade>=80:
    print('B')
elif grade>=70:
    print('C')
elif grade>=60:
    print('D')
elif grade>=50:
    print('D')
else:
    print('F')

