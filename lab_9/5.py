# 5. Modify “lab9_5.py” to check for a duplicate key before saving a new item in the dictionary. In
# case an item is already available in the students_dict, then the program should warn the user.

dic = {'rauf': 'jatoi'}
k = input('Enter key: ')
v = input('Enter Value: ')

if k in dic:
    print('Key is already in the dictionary.')
else:
    dic[k] = v

print(dic)
