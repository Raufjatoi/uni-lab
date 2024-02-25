#Task 2: Write a program that takes your name and father name and describe it in a message of your 
#choice.
def describe_name(name, father_name):
    message = f"My name is {name} and my father's name is {father_name}."
    return message

name = input("Enter your name: ")
father_name = input("Enter your father's name: ")

print(describe_name(name, father_name))
