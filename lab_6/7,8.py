#7. Write a Python program to convert a list of characters into a string.
c = ['a','b','c','d']
r = ''.join(c)
print(r)

#8. Write a program that randomly selects an item from list_1 and then maps it to a 
#randomly selected item of list_2
import random 
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print("Before:")
print("List 1:", l1)
print("List 2:", l2)
r1 = random.choice(l1)
r2 = random.choice(l2)
index1 = l1.index(r1)
index2 = l2.index(r2)
l1[index1] = r2
l2[index2] = r1
print("After:")
print("List 1:", l1)
print("List 2:", l2)
