def lcm (a,b):
    g = a if a>b else b
    while True: 
        if g%a == 0 and g%b ==0 :
            return g
        g +=1
num1 = int(input('enter num : '))
num2 = int(input('enter num2 : '))
print(f'the lcm of {num1} and {num2} is {lcm(num1,num2)}')