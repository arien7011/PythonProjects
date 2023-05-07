#snake water game

import random
def winnerofgame(comp,user) :
    if comp == user :
        return None
    elif comp == 's' :
        if user == 'w' :
            return False
        elif user == 'g' :
            return True
        elif comp == 'w' :
            if user == 's' :
                return False
            elif user == 'g' :
                return True
            elif comp == 'g':
               if user == 's':
                return False
            if user == 'w' :
                return True
                

print("computer turn : 's' ,'w' , 'g'")
rndm = random.randint(1,3)
if rndm == 1 :
  comp = 's'
elif rndm == 2 :
    comp = 'w'
elif rndm == 3 :
    comp = 'g'

user = input("Enter 'snake' 'water' 'gun' ")
a = winnerofgame(rndm,user)

print(f"You chose {user}")
print(f"comp chose {rndm}")
if a == None :
    print('Game tied')
elif a:
    print('You won ')

else :
    print('You lose')