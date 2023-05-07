# A spam comment is defined as text containing following keywords
# ' make a lot of money' , "buy now" ,"subscribe this" , "click this"

comment = input('Enter the comment : ')
if('make a lot of money' in comment) :
    spam = True
elif('buy now' in comment) :
    spam = True
elif('click this' in comment) :
    spam = True
elif('subscribe this' in comment) :
    spam = True
else :
    spam = False

    if(spam == True) :
        print('This is spam')
    else :
        print('This is not spam')
        