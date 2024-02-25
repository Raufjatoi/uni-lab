# 5. 4. Create "lab10_5.py". Write a Python program that takes user input for a sentence containing
# underscores. Utilize the lstrip() method to remove these leading characters and display the cleaned
# sentence.
r = input(' Enter a sentence with starting of underscores : ')
s = r.lstrip('_')
print(s)