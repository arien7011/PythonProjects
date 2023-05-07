#Write a program to accept marks of five students in a sorted manner

m1 = int(input('Enter marks of st1 : '))
m2 = int(input('Enter marks of st2 : '))
m3 = int(input('Enter marks of st3 : '))
m4 = int(input('Enter marks of st4 : '))
m5 = int(input('Enter marks of st5 : '))
m6 = int(input('Enter marks of st6 : '))
m7 = int(input('Enter marks of st7 : '))

studentMarksList = [m1,m2,m3,m4,m5,m6,m7]
studentMarksList.sort()
print(studentMarksList)