#Write a program to find whether a username contains less than 10 characters or not

username = input('Enter your username')

if(len(username)<10) :
    print('username contains less than 10 characters')
else :
    print('username contains more than 10 characters')