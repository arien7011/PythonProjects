#Write a program to multiply table of n in reverse order

num = int(input('Enter the number : '))
l1 = []
for i in range(1,11) :
    l1.append(num*i)
count = 10
for i in reversed(range(10)) :
    print(f"{num}*{i+1}={l1[i]}")


## SOl:-1
# l1 = []
# for i in range(1,11) :
#     l1.append(num*i)
#     if(i==10):
#         break
# l1.reverse()
# print(l1)
# for i in range(10) :
#     print(l1[i])
    # print(f"{num}*{i}={l1[i]}")