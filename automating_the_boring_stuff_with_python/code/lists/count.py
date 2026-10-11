def count_order():
    print("Give some numbers (max 10 numbers in single digit): ")
    
    numbers = input().split()
    stored = []

    for number in numbers[:10]:
        stored.append(int(number))

    print(stored)

    print("Do you want to see the numbers in reverse? (Yes/No)")
    yes_no = input()
        
    if yes_no.lower() == 'yes' or yes_no.lower() == 'y':
        stored.reverse()
    
    print(stored)

count_order()