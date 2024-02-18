# 6. Create “lab7_4.py”. Write a program that inputs username and password from the user, and then matches
# with the stored username:password in a dictionary. The program welcomes the user if the username and
# password are correct and regrets when wither username or password is incorrect.
dic = {'rauf': 1234}
a = input('Enter name :')
p = int(input('Enter password :'))
for key,value in dic.items():
    if a == key and p == value:
        print('welcome user')
    else:
        print('not welcome user')