# Very ineficient but fun and it wasn't needed at all, but it tought me a bit 
# about state and del()

# Retrieve capital: to retrieve all capital letters from A...Z
def retrieve_capital(capital):
    # Append such that there's a set of indices in capital
    while len(capital) < 26:
        capital.append(0)

    a = 65
    
    i = 0

    # Initialize the indices with the values A...Z
    while i < 26:
        capital[i] = a
        a += 1
        i += 1

    return capital

# Retrieve small: to retrieve all small letters from a...z
def retrieve_small(small):
    # Append such that there's a set of indices in small
    while len(small) < 26:
        small.append(0)
    
    a = 97

    i = 0

    # Initialize the indices with the values a...z
    while i < 26:
        small[i] = a
        a += 1
        i += 1

    return small

# playable_state: decrease and expand capital and small such that name
# gets filled with the indexes in capital and small
#
# To retrieve the wanted name, and return name
def playable_state(capital, small, wanted):
    c_state = retrieve_capital(capital)
    s_state = retrieve_small(small)

    name = []

    for char in wanted:
        # Get the capital characters for wanted/name
        if char >= 'A' and char <= 'Z':
            i = 0
            while chr(c_state[i]) != char:
                del c_state[i]

            name.append(c_state[i])

            c_state = retrieve_capital(capital)

        # Get the small characters for wanted/name
        else:
            j = 0
            while chr(s_state[j]) != char:
                del s_state[j]
            
            name.append(s_state[j])

            s_state = retrieve_small(small)
    
    return name

capital = []
small = []
wanted = ['L', 'u', 'u', 'k']

name = playable_state(capital, small, wanted)

for char in name:
    print(chr(char), end='')