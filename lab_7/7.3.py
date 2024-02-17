# 3. Modify “lab7_1.py” to use a unique key for each record. This way, every student will be assigned a 
# unique number and two students with same name can be added to the students_dict.
dic = {}
for i in range (5):
 student = input('Enter name : ')
 id = input('Enter unique id : ')
 if student in dic and id == dic[student]:
    print('already exist')   
 else:
    if student in dic: 
      print('student already exist but with diff')
    dic[student] = id
print(dic)
