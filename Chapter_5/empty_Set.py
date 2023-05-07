## Note** Here comments with two hash are notes comments and single hash comments are codes
##Important: This syntax will create an empty dictionary and not an empty set
a = {}
# print(type(a))
# print(a)

##Note : An empty set can be created using the below syntax

b = set()
# print(type(b))

##Adding values in empty set
b.add(4)
b.add(5)
b.add(4) ## you cannot add duplicate value in sets
# print(b)

# b.add({4:5}) 
# b.add([3,4,5])
# print(b)
## dictionary and list cannot be added or stored in 'sets' because they are unhashable type that means 
## dictionary items and list items can be changed
## But the values in sets cannot be changed

b.add((3,4,5)) #Here we added a tuple so we can add a tuple in a set because tuple items cannot be changed so it is a hashable type
# print(b)

##remove() removes the element from the set
b.remove(4) 
# b.remove(15) #throws an error because '15' is not present in the set

##pop() used to remove arbitary(random i.e from any element in the set irrespective of their position) element from the set
print(b.pop())
##Length of the set
print(len(b)) # prints the length of the set
print(b)