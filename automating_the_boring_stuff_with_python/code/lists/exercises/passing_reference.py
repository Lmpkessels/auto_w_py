import copy

def passing_arguments(some_list, copy_param):
    some_list.append(copy_param)

some_list = []
copy_param = 'Hello'

passing_arguments(some_list, copy_param)
print(some_list)

copy_of_some_list = copy.copy(some_list)
print(copy_of_some_list)

two_d_list = [[0, 1, 2], [1, 1, 1], [2, 3, 1]]
copy_of_two_d_list = copy.deepcopy(two_d_list)
print(copy_of_two_d_list)