# program to convert celcius to fahrenheit
def findCelcius(cel) :
    return (cel)*(9/5) +32
celcius = int(input('Enter temperature in fahrenheit : '))
cel = findCelcius(celcius)
print(f"38F is equal to {cel} celcius")