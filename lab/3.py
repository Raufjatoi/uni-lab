#Task 1: Write function that takes N numbers as inputs and return sum of all those numbers.
def sum_of_numbers(*args):
    return sum(args)

numbers_sum = sum_of_numbers(1, 2, 3, 4, 5)
print("Sum of numbers:", numbers_sum)
