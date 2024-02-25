# 3. Create “lab11_3.py”. Write a program with a function that takes two numbers as input and returns the 
# greatest common divisor (GCD). For two numbers a and b, the GCD is the largest number that divides 
# both a and b.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The greatest common divisor (GCD) of", num1, "and", num2, "is:", gcd(num1, num2))
