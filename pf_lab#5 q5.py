#Create “lab5_5.py” and write a program that when runs, reads input typed the user and quits only when
#user types a ‘quit’ character.

while True:
    a = input("enter somethin :: ").lower()
    print(a)
    if a == "quit" or a == "q":
        break