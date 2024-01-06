#Create “lab5_9” and write a program that lets user enter 10 (later any number of) numbers and then count
#how many were odd and even.
e = 0
o = 0
for i in range (10):
    a = int(input("enter a num :: "))
    if a % 2 ==0:
        e +=1
    else:
        o+=1
    i+=1
print('even num are ', e)
print('odd nums are ', o)