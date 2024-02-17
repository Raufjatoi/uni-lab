student = {}
for i in range (1,3):
    num= input('Enter number :  ')
    name= input('Enter name :  ')
    student[name] = num
x = input ('enter name : ')
if name in student.keys():
    print(f" {student[x]} is already submitted ")
else:
    print("adding the name ")

    
