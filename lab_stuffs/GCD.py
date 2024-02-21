def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input('Enter num: '))
num2 = int(input('Enter num 2: '))
print(f'The GCD is: {gcd(num1, num2)}')
