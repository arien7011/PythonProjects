#write a program to greet the user with "Good Day" using function
def greetme(name) :
    return "Good Day " + name

#Note:- Default parameter value - this value can be used as a  default argument in a functioon
#  when no argument is passed to the function
#example
def greetmetoday(name="Arian") :
    return "Good Morning " + name



name = (input("Enter your name : "))
# name.upper()
# print(f"{greetme()} {name.upper()}")
print(greetmetoday())