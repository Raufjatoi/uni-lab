# 1. Open Python IDLE terminal and then create a new file. Name it “lab7_1.py”. Write a program that asks 
# the user for student’s name and obtained marks for 10 students and then stores them in a dictionary.
dic = {}
for i in range (10):
    name = input('Enter name : ')
    marks = int(input('Enter marks : '))
    dic[name] = marks
print(dic)