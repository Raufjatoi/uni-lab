#Create “lab5_10” and write a program that prints Fibonacci series.
a,b = 1,2
print(a, b ,end=" ")
for i in range(2,16):
    c = a + b 
    print(c , end=" ")
    a,b = b,c