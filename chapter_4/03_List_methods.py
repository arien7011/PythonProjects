#Methods of List

items = [23, 34, 343, 434 ,543 ,22]
#sort the list
items.sort() #sorts the list
print(items)

items.reverse()
print(items) #reverse the list items

items.append(39)
print(items) #it adds the element in the list

items.insert(0,50) #it insert an element on the given index
print(items)

items.pop(0) #it remove the element from the given index from the list 
print(items)

items.remove(543) #it removes the given element from the list
print(items)