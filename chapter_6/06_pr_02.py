# Write a program to find out whether a student is pass or fail if it requires total 40 % and atleast 33% in each subject to pass
# assume any three subject and take marks input for those subject

m1 = int(input('Enter marks in Maths : '))
m2 = int(input('Enter marks in Hindi : '))
m3 = int(input('Enter marks in Sanskrit : '))

## sol :1
if(m1<33 or m2 < 33 or m3 < 33) :
    print('You are failed because of less than 33% marks in one of the subjects')

elif((m1+m2+m3)/3 <40) :
    print("You're failed because you have got less than 40 percent in your exams")

else :
    print("Congratulations !! you have cleared the exam")

## sol:2
# if(m1 >= 33 and m2 >=33 and m3 >= 33) :

#  avg_per = ((m1+m2+m3)/300)*100

#  if(avg_per >=40) :
#   print('You are pass')
#  else :
#   print('you are fail')

## sol:3
# avg_per = ((m1+m2+m3)/300)*100

# if ((m1 >= 33 and m2 >= 33 and m3 >= 33) and avg_per >= 40):
#   print('You are pass')
# else :
#   print("you're fail")