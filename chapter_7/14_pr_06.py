#Write a program to find the factorial of a given number
n = int(input('Enter the number : '))
##sol:2
factorial = 1
for i in range(1,n+1) :
    factorial = factorial*i
   
print(f"The factorial of {n} is {factorial}")
  
## Sol:2 factorial = 1
# for i in range(1,n+1)  :
#     if(n == 1) :
#         print('1')
#     elif(i<=n) :
#      factorial = factorial*i
# else :
#     print(f"The factorial of {n} is {factorial}")