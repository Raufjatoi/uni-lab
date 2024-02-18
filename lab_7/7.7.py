# 7. Create “lab7_5.py”. Write a program that lets the user input a sentence and then finds the frequency of
# alphabets in the entered sentence. The output should be similar to the following
def count_alphabets(sentence):
    sentence = sentence.lower()
    frequency = {}
    for char in sentence:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    
    return frequency

sentence = input("Enter a sentence: ")
alphabet_frequency = count_alphabets(sentence)

# Print the frequency of each alphabet
print("Frequency of alphabets:")
for alphabet, count in sorted(alphabet_frequency.items()):
    print(f"{alphabet} - {count}")


