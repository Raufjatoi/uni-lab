# 2. Create “lab8_2.py”. uses the max() and min() functions. Ask the user to input three numbers and find the
# maximum and minimum values among them.
l = []
for i in range(3):
    n = int(input('Enter num : '))
    l.append(n)

def minimum(a):
    return min(a)

def maximum(a):
    return max(a)

print(f'max num is {maximum(l)}')
print(f'min num is {minimum(l)}')


