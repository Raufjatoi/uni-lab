#1. Open Python IDLE terminal and then create a new file. Name it “lab6_1.py”. Write a program that
#generates a list of odd numbers from 1 to 1000, prints numbers and then prints the sum of numbers.
for i in range(1,1001,2):
        print(i)

#2. Create “lab6_2.py”. Write a program that generates a list of 20 random numbers, prints the list and then 
#finds the (1) largest number, and (2) smallest number using linear search method.
for j in range(0,1001,2):
    print(j)

#3 Create “lab6_3.py”. Write a Python program that prompts the user to enter 5 numbers, stores them in a 
#list and then prints the sum of all even numbers in the list

l = []
for _ in range(5):
    num = int(input("Enter number: "))
    l.append(num)
print("Numbers entered:", l)
even_numbers = [i for i in l if i % 2 == 0]
print("Even numbers:", even_numbers)
even_sum = sum(even_numbers)
print("Sum of even numbers:", even_sum)

#4. Create “lab6_4.py”. Create a tuple containing the names of 5 countries. Write a program that iterates 
#through the tuple and prints only the countries with a length greater than 7 characters.

c = ('pakistan', 'india','japan','china','indonesia')
for i in c:
     if len(i) > 7:
       print(i)
