#wirte a python function to print the first n lines of the  following pattern

#  ***
#  **
#  *

# method:1 def printpattern(number) :
#     for i in reversed(range(1,number+1)):
#         print("*"*i)


#method :2
def printmypattern(number) :
    for i in range(number) :
        print("*"*(number-i))

        
printmypattern(3)
# printpattern(4)