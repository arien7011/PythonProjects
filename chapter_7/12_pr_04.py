#write a program  to find whether a given number is prime or not

num = int(input('Enter the number : '))
prime = True
for i in range(2,num) :
    if(num%i == 0) :
        prime = False
        break 
    if prime :
        print('It is a prime number')
    else :
        print('It is not a prime number')
# for i in range(2,num) :
#  Sol:1  if(num == 2) :
#         print('It is a prime number')
#     elif(num%i == 0) :
#         print('It is not a prime number')
#         break 
#     else :
#         print('It is a prime number')
