# For lists the values within taken for comparison can be the same,
# but order matters and comparison equals False
list1 = ['Hello', 'World', 'New', 'Age']
list2 = ['World', 'New', 'Hello', 'Age']

list_bool_v = list1 == list2

print(list_bool_v)

# Dictionaries equal True if the keys and values taken in comparison
# are the same, order doesn't matter 
dict1 = {'Name': 'Luuk', 'Age': 26, 'Lastname': 'Kessels'}
dict2 = {'Lastname': 'Kessels', 'Name': 'Luuk', 'Age': 26}

dict_bool_v = dict1 == dict2

print(dict_bool_v)