#write a program to fill in a letter template with name and date 
from datetime import date

letter = ''' Dear <|NAME|>,
I'm Jackie from ABC company and hereby to inform you that You are selected!
<|DATE|>]
Have a great day ahead !
Thanks and regards
Anna
'''
name = input('Enter your name:\n')
today_date = input('Enter today date:\n')
letter = letter.replace('<|NAME|>' , name)
letter = letter.replace('<|DATE|>',today_date)
print(letter)