#9. Create “lab6_9.py”. Write a Python program that takes a list of student names and their corresponding 
#grades as key-value pairs in a dictionary. The program should then prompt the user to enter a student 
#name, and it should output the grade associated with that student. If the student is not found in the 
#dictionary, the program should print a message saying "Student not found.
students = {'rauf' : 'A',
           'adil': 'B',
           'farhan': 'c',}
a = input("enter name : ").lower()
if a in students:
    print(students[a])
else:
    print("students didnt found")