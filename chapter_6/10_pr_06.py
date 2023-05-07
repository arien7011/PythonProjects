#Write a program to calculate the grade of the student form his marks from the following scheme
# 90-100 -> ex , 80-90 -> A, 70-80 -> B , 60-70 -> C , 50-60 -> D

marks = int(input('Enter your marks to convert them to grade : '))

##Sol:1
if marks >= 90 :
    Grade = 'excellent'
elif marks >=80 :
    Grade = 'A'
elif marks >=70 :
    Grade = 'B'
elif marks >=60 :
    Grade = 'C'
elif marks >=50 :
    Grade = 'D'

else :
    print('You are fail')
    
    
print('Your grade is ' + Grade)


    

## Sol:2
# if(marks>=90 and marks <= 100) :
#     print('Grade -> Ex')

# elif(marks>=80 and marks <= 90) :
#     print('Grade -> A')
# elif(marks >=70 and marks <=80) :
#     print('Grade -> B')
# elif(marks >=60 and marks <=70) :
#     print('Grade -> C')
# elif(marks >=50 and marks <= 60) :
#     print('Grade -> D')

# elif(marks<50) :
#     print('Grade -> F')

# else :
#     print('Grade is none')