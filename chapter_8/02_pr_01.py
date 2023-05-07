#Write a function to find the greatest of three numbers
#method:1
def find_greatest(n1,n2,n3) :
    l1 = [n1,n2,n3]   
    greatest = max(l1)
    return greatest

 
# print(find_greatest(3,4,5))
# greatest_num 
# print(find_greatest(3,4,5))

#method :2

def findMaximum(n1,n2,n3) :
    if(n1>n2) :
        if(n1>n3) :
            return n1
        else :
            return n3
        
    else :
        if(n2>n3) :
            return n2
        else :
         return n3
    

max = findMaximum(4,6,9)
print('The greatest number of all three is :'+ str(max))