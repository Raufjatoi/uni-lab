list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
list_3 = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'melon', 'pear', 'peach', 'plum', 'strawberry']
zipped_lists = zip(list_1, list_2, list_3)
for items in zipped_lists:
    print(items)


# Example using append
list_1 = [1, 2, 3]
list_1.append(4)
print(list_1)  # Output: [1, 2, 3, 4]

# Example using extend
list_2 = [5, 6, 7]
list_2.extend([8, 9, 10])
print(list_2)  # Output: [5, 6, 7, 8, 9, 10]


grocery_list = ['flour','cheese','carrots']
for idx,val in enumerate(grocery_list):
 print("%s: %s" % (idx, val))

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

items=[3,45,66,5,90,101]
items2=[55,77]
items.remove(5)
print(items)
items.extend(items2)
print(items.pop(6))
