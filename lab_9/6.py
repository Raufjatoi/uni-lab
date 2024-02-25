# 6. Create "lab9_6.py". Write a program that takes a sentence as input and uses the split() function to
# split the sentence into words. Then, reverse the order of words in the sentence and print the
# modified sentence.
s = input('Enter sentence: ')
ss = s.split()
r = ' '.join(ss[::-1])
print(r)
