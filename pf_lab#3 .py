"""
sub1 = int(input("Enter first sub marks :: "))
sub2 = int(input("Enter 2nd sub marks :: "))
sub3 = int(input("Enter 3rd sub marks :: "))
avg = sub1 + sub2 + sub3 / 3
per = sub1 + sub2 + sub3 / 100
grade = ()
if per >81:
    grade = ("A")
elif per >=70:
    grade = ("B")
elif per >=60:
    grade = ("C")
elif per <60:
    grade = ("D")
print(f"Ur avg is {avg}")
print(f"ur grade is {grade}")
print(f"ur percent is {per}%")
"""
'''
## Bard 

sub1 = int(input("Enter first sub marks: "))
sub2 = int(input("Enter 2nd sub marks: "))
sub3 = int(input("Enter 3rd sub marks: "))

avg = (sub1 + sub2 + sub3) / 3  # Added parentheses for correct calculation
per = (sub1 + sub2 + sub3) / 100  # Added parentheses for correct calculation

grade = ""  # Initialize grade as an empty string

if per >= 81:
    grade = "A"
elif per >= 70:
    grade = "B"
elif per >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Your average is {avg:.2f}")  # Format average to 2 decimal places
print(f"Your percentage is {per:.2f}%")  # Format percentage to 2 decimal places
print(f"Your grade is {grade}")

'''
### CHATGPT 
sub1 = int(input("Enter first sub marks: "))
sub2 = int(input("Enter 2nd sub marks: "))
sub3 = int(input("Enter 3rd sub marks: "))

avg = (sub1 + sub2 + sub3) / 3

# Corrected calculation for percentage
percentage = (avg / 100) * 100

grade = ""  # Initialize grade as an empty string

if percentage >= 81:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Your average is {avg:.2f}")
print(f"Your percentage is {percentage:.2f}%")
print(f"Your grade is {grade}")