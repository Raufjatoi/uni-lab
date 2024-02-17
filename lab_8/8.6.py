# 6. Create "lab8_6.py". Implement a program using the type() function to determine the data type of a userinputted value.
u = input('Enter somethin : ')
def is_type(x):
    return type(x)
print(f'type of {u} is {is_type(u)}')