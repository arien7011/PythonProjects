# Continue statement in loops

# for i in range(8) :
#     if i== 5 :
#         continue
#     print(i)

##Important note :- continue is used to skip values here it skips 5 and prints all the range items , so you can use continue
# statement when you want to escape any items in the list ,tuples or iterables etc. 

userInfo = ['aman','mishra','amanmishra343@gmail.com', '23-09-2002']

for item in userInfo :
    if item == 'mishra' :
        continue
    print(item)