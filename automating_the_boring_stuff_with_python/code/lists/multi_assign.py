# Use a list to create multiple variables, with multi assign

full_name = ['Luuk', 'Martinus Petrus', 'Kessels']
first, middle, last = full_name

print("The full name is:", first, middle, last)

print(first + "'s", "holy names are:", middle)

import random

print("Please provide your name to finish your order: ")
order_placed = input()

if order_placed:
    order_n = random.random()

order = ['Cup', f'{order_n}', '$2.99', '6']
item, o_num, price, stock = order

print(f"{order_placed} ordered:", item, "at", price)
print("The order number is:", o_num)

multi = [
    'With', 'multi', 'assign', 'you', 'can', 'use', 'a', 'list',
    'for', 'assigning', 'multiple', 'values', 'to', 'create', 
    'variables'
]

(withh, multii, assign, you, can, use, a, listt, forr, assigning,
multiple, values, to, create, variables) = multi
print(withh, multii, assign, you, can, use, a, listt, forr, assigning,
multiple, values, to, create, multiple, variables)