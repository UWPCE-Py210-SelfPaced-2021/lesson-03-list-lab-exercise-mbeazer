#!/usr/bin/env python

# Series 1
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
response = input('Add another fruit: ')
fruit_list.append(response)
print(fruit_list)

num_response = input('Choose a number: ')
print(num_response + ' ' + fruit_list[int(num_response) - 1])

fruit_list = ['Papaya'] + fruit_list
print(fruit_list)

fruit_list.insert(0, 'Pumpkin')
print(fruit_list)

for fruit in fruit_list:
    if fruit[0] == 'P':
        print(fruit)

# Series 2
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
fruit_list.pop(-1)
print(fruit_list)

del_response = input('Which fruit would you like to remove?: ')
for fruit in fruit_list:
    if del_response in fruit_list:
        if del_response == fruit:
            fruit_list.remove(fruit)

print(fruit_list)

# Series 3
"""Iterating through a reversed list so that the index change of the removed elements does not affect the next in
sequence """
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
for fruit in reversed(fruit_list):
    like_response = input('Do you like {:s}?: '.format(fruit.lower()))
    while like_response != 'yes' and like_response != 'no':
        like_response = input('Please enter "yes" or "no": ')
    if like_response == 'no':
        fruit_list.remove(fruit)
print(fruit_list)

# Series 4
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_list_s4 = []
for fruit in fruit_list:
    fruit_list_s4.append(fruit[::-1])
fruit_list.pop(-1)
print(fruit_list)
print(fruit_list_s4)
