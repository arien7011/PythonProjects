#Write a program to create a dictionary of Hindi words with their english translation and  provide user
# with an option to look at up

myDict = {
    'pankha' : 'Fan',
    'vastu' : 'item',
    'chalak' : 'clever'
}

print('Here are the words in the dictionary : ' , myDict.keys())

words = input('Enter the word to see the translation :\n ' )
# print('we found : ' ,myDict[words]) it will throw an error in case the word is not present in the dictionary
#Below line will not throw an error if word is not present because we are accessing the word in the dictionary using get which 
#return none if item is not present
print('we found : ' ,myDict.get(words))
