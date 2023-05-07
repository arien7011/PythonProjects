#Write a program to find the greatest of four numbers entered by the user

n1 = int(input('Enter first number : '))
n2 = int(input('Enter second number : '))
n3 = int(input('Enter third number : '))
n4 = int(input('Enter fourth number : '))

# sol:1
# if(n1>n2 and n1>n3 and n1>n4) :
#     print(str(n1)+ ' is greater')

# elif(n2>n1 and n2>n3 and n3>n4) :
#     print(str(n2)+' is greater')

# elif(n3>n1 and n3>n2 and n3>n4) :
#     print(str(n2) + ' is greater')

# elif(n4>n1 and n4>n2 and n4>n3) :
#     print(str(n2) +' is greater')

#sol : 2
if(n1>n4) :
    f1 = n1
else :
    f1 = n4

if(n2>n3) :
    f2 = n2
else :
    f2 = n3

    if(f1>f2) :
      print( str(f1) + ' is greatest')
    else :
        print( str(f2) + ' is greatest')

