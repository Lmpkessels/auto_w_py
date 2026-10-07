def retrieve_alpha(capital, small):
    a = 96
    z = 121
    
    i = 0

    while a <= z:
        a += 1
        capital.append(a-32)
        small.append(a)
        i += 1

def retrieve_name(capital, small, name, wanted):
    retrieve_alpha(capital, small)

    for letter in wanted:
        for i in range(len(capital)):
        
            if chr(capital[i]) == letter:
                name.append(capital[i])
                break
        
            if chr(small[i]) == letter:
                name.append(small[i])
                break

    # There's a funny bug, because k < L in terms of index, so
    # L is reinitialized to k which equal kLuu instead of my name
    # 
    # TODO: find a way to prevent this

    for j in range(len(name)):
        print(chr(name[j]), end='')

capital = []
small = []
name = []
wanted = ['L', 'u', 'u', 'k']

retrieve_name(capital, small, name, wanted)