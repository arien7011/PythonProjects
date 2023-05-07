#Write a function to print the sum of n natural numbers using recursion

#n! = (n-1)! *n
#sum(n) = (n-1) + n

def findSum(num):
    sum = 0
    for i in range(1,num+1) :
     sum+= i
     if(i==num) :
        return sum


number= int(input('Enter your number : '))
totalsum = findSum(number)
print(f'the sum of first {number} natual number is ' +str(totalsum))