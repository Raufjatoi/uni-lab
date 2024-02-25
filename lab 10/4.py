# 4. Create "lab10_4.py". Initialize a string variable with a sentence containing whitespaces at various
# positions. Write a program that uses the strip() function to remove all whitespaces from the
# sentence and prints the modified string.
r = input('Enter sentences with #! words anywhere : ')
s = r.strip('#@!$')
print(s)