#Dictionary Methods


myDict = {
    'name' : 'Arian',
    'marks' : 45,
    'studentList' : ['Arian','Jacky','Challen'], #we can store a list
    'anotherDict' : {'name' :'Shiva', 'marks': 45} #we can store nested dictionary

}

# 1. To get all keys of the dictionary
# print(myDict.keys())
# 2. To get all the values of the dictionary
# print(myDict.values())
# 3. To get all the content(in key value pairs) of the dictionary inside the tuple 
# print(myDict.items()) 

#4. TO update the dictionary items
updatedValue = {
   'name' : 'Arian',
    'freind' : 'Vishal',
    'Mentor' : 'Shailesh Sir'
 }
myDict.update(updatedValue) #Update the dictionary by adding key value pairs from updateValue
# print(myDict)
print(myDict.get('name')) #print value associated with arian
#Difference between get method and [] ewhich we used to access the values of dictionary
print(myDict.get('fruit'))  #it will give me the 'none' as fruit is not present in the dictionary 
print(myDict['fruit'])      #it will give me the key error because fruit key doesn't exist in the given dictionary

