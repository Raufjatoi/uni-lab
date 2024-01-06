#Create “lab5_8” and write a program that prints divisible numbers of a given number.
num = int(input("enter a num : "))
for i in range(1, num + 1):
  if num % i == 0:
    print(i, end=" ")

       
