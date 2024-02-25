# 4. Modify “lab11_3.py”. Make the user-defined function compute either GCD or least common multiple 
# (LCM). The function now takes three arguments i.e., two numbers and a string with either “lcm” or “gcd”
# value and then returns the answer accordingly.
num1 = int(input('Enter a num : ')) 
num2 = int(input('Enter anotherr num : '))
c = input('chose lcm or gcd : ').lower()
def gcd (a,b):
    while b :
        a , b = b , a % b 
        return a 
def lcm (a,b):
    greatest = a if a>b else b 
    if ( greatest % a == 0 and greatest % b == 0 ):
        return greatest
    greatest += 1
if c == 'gcd' :
    print(gcd(num1,num2))
elif c == 'lcm' :
    print(lcm(num1,num2))
else:
    print('invalid')