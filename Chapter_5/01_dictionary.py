#Dictionary is a container or data structure in python who stores data in a key value pairs 

#Define a dictionary

myDict = {
    'name' : 'Arian',
    'marks' : 45,
    'studentList' : ['Arian','Jacky','Challen'], #we can store a list
    'anotherDict' : {'name' :'Shiva', 'marks': 45} #we can store nested dictionary

}

# print(myDict['name'])  #accessing the data using keys from the dictionary
# print(myDict['studentList']) 
print(myDict['anotherDict']['name'])