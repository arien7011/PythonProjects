#Write a program to find the sum of first n natural numbers using for loop

num = int(input('Enter the number : '))
sum = 0 
i = 1
while i<num+1 :
    sum += i
    i+=1
    
print(sum)