def retrieve_alpha(capital, small):
    a = 96
    z = 121
    
    i = 0

    while a <= z:
        a += 1
        capital.append(a-32)
        small.append(a)
        i += 1

def retrieve_name(capital, small, name):
    retrieve_alpha(capital, small)

    for i in range(len(capital)):
        if chr(capital[i]) == 'L':
            name.append(capital[i])
        if chr(small[i]) == 'u':
            name.append(small[i])
            name.append(small[i])
        if chr(small[i]) == 'k':
            name.append(small[i])

    # There's a funny bug, because k < L in terms of index, so
    # L is reinitialized to k which equal kLuu instead of my name
    # 
    # TODO: find a way to prevent this
    print(chr(name[0]) + chr(name[1]) + chr(name[2]) + chr(name[3]))

capital = []
small = []
name = []

retrieve_name(capital, small, name)