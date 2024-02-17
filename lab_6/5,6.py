#5. Create “lab6_5.py”. Generate a list of 50 integers. Write a program that iterates through the list and prints 
#the square of each number if it's even, and the cube if it's odd.
l = []
for i in range (1,51):
    l.append(i)
print(l)
for i in l:
    if i % 2 == 0:
        print(i**2)
    else:
        print(i**3)

## if random nums 
import random

# Generate a list of 50 random integers
l = [random.randint(1, 100) for _ in range(50)]
print("Original list:", l)

# Iterate through the list and print the square for even numbers and cube for odd numbers
for num in l:
    if num % 2 == 0:
        print(f"Square of {num}: {num**2}")
    else:
        print(f"Cube of {num}: {num**3}")

#6. Create “lab6_6.py”. Write a program that takes two sets as input and prints the union of the two sets.

set1 = set()
set2 = set()

for i in range (3):
    a = int(input("Enter num for set1 : "))
    b = int(input("Enter num for set2 : "))
    set1.add(a)
    set2.add(b)
set3 = set1.union(set2)
print(set3)

