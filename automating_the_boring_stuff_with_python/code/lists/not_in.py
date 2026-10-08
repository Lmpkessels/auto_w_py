# Use in and not to determine if a value is or isn't a value in a list

full_name = ['Luuk', 'Martinus', 'Petrus', 'Kessels']
if 'Luuk' and 'Martinus' and 'Petrus' and 'Kessels' in full_name:
    print("The full name is: ")
    
    for name in full_name:
        print(name, end=' ')
else:
    print("Full name is incomplete")

print("\n")

greet_world = ['Hello', '','New', 'World']
if 'Brand' not in greet_world:
    greet_world[-3] = 'Brand'

for greet in greet_world:
    print(greet, end=' ')

numbers = [3, 2, 1, 0]
if -1 not in numbers:
    numbers.append(-1)

for number in numbers:
    print('\n', number, end=' ')