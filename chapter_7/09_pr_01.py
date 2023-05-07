#Wirte a program to print multiplication number of a given  number using for loop

n = int(input('Enter the number : '))
for i in range(1,11) :

  #sol:1  # print(str(n) + 'x' + str(i) + '=' + str(n*i))
  #sol:1  # print(n*i)
  #sol:3 using 'f' string you can use any element and can evaluate any expression inside the string using curly braces
    print(f"{n}'x'{i}= {n*i}")
