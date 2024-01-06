#Create “lab5_7.py” and write a program that determines whether a number (entered by the user) is prime
#or not.

n = int(input("Enter a number : "))
if n > 1:
    for i in range(2,n):
        if i % n == 0:
            print(f"{n} is not a prime number")
            break
        elif i % n != 0:
            print(f"{n} is prime number")
            break
else:
    print(f"{n} is not a prime number")



