# 2. Modify “lab7_1.py” to check for a duplicate key before saving a new item in the dictionary. In case an 
# item is already available in the students_dict, then the program should warn the user.
dic = {}
for i in range (10):
    std = input('Enter student : ')
    marks = input('Enter marks : ')
    if std in dic :
        print('already exist ')
    else:
     dic[std] = marks