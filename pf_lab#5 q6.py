##reate “lab5_6.py” and write a program that computes the factorial of a number entered by the user.

num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("The factorial of", num, "is", factorial)






"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
f = int(input("Enter a number: "))

# Calculate factorial and display the result
fact = factorial(f)
print(f"The factorial of {f} is: {fact}")



"""

 
