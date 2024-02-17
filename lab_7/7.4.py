# 4. Create “lab7_2.py”. Consider the following dictionary that contains the items id and item’s price in a 
# shop:
# Item_dict={‘item_1’: 45.50, 'item_2':35, 'item_3': 41.30, 'item_4':55, 'item_5': 24}
# Write a program that finds the item with (1) highest price, and (2) smallest price.

Item_dict={'item_1': 1000, 'item_2':35, 'item_3': 41.30, 'item_4':55, 'item_5': 00}
max = 0
min = 100
for value in Item_dict.values():
    if value > max:
        max = value 
    elif value < min:
        min = value 
print(Item_dict)
print(f'max value is {max}')
print(f'min value is {min}')

