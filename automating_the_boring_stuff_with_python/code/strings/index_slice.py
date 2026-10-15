string = "Hello, world!"

# Using a for loop to retrieve positive indices
def print_pos_indx(string):
    indx = -1
    for char in string:
        indx += 1
        print(char, "Index: " + str(indx))

# Using a for loop to retrieve negative indices
def print_neg_indx(string):
    n = len(string)
    indx_n = -1 - n
    for char in string:
        indx_n += 1
        print(char, "Index: " + str(indx_n))

print_pos_indx(string)
print('\n')
print_neg_indx(string)

# Using slicing to retrieve characters
h = string[0] # Returns H
print(h)

hello = string[:5]
print(hello)

world = string[7:-1]
print(world)
world = string[-6:-1]
print(world)

comma = string[5]
print(comma)
comma = string[-8]
print(comma)

space = string[6]
print(space)