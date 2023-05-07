#String is a sequence of characters enclosed within quotes
# strings in python can be represented and can be used  differently for different styles of words  as 
#  'hello' 

# "Arien's"

# '''Hey How 
# # you doing '''  

name = 'nameet'
#access character in strings
print(type(name))
print(name[2])

#slicing in python (part of the strings)
print(name[1:3])
print(name[1:6])
print(name[1:]) #it is same as name[1:6]
print(name[:6])
print(name[-1])
c = (name[-6:]) #it is same as [1:4]
print(c)

#skipping characters in strings
sentence = "Helloworld"

print(sentence[0:6:2]) 
# so the third number represents skipped values that means it will print
#every second character in the string sequence
print(sentence[0::3])