###      MAJOR ASSIGNMENT      ###
alphabet = 'abcdefghijklmnopqrstuvwxyz'
hint = 'xznlwebgjhqdyvtkfuompciasr'

secret_message = input('Enter your message: ')
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():#Checks if every character of the string is a letter
        print(hint[alphabet.index(c)],end='')
    else:
        print(c, end='')
