# 4. Create "lab9_4.py". Write a program that takes a string as input from the user and uses the split()
# function to split the string into words. Then, use a dictionary to count the frequency of each word
# in the string.
def count_word_frequency(sentence):
    words = sentence.split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

def main():
    user_input = input("Enter a sentence: ")
    word_frequency = count_word_frequency(user_input)
    print("Word frequencies:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
