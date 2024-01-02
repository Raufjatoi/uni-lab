#1
while True:
 a = int(input("Enter a number :"))
 if a % 2 == 0:
    print("Number is even")
 elif a == 0:
    print("Number is zero")
 elif a < 0:
    print("Number is negative")
 else:
    print("Number is odd")