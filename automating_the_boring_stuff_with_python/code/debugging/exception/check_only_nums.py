def check_only_numbs(numbers):
    for number in numbers:
        if not isinstance(number, int):
            raise Exception("There should be only numbers in the array of numbers")
        else:
            print(number)

try:
    check_only_numbers([1, 2, 4, 1])
    check_only_numbers([1, "Hello", 2, 3])
except Exception as err:
    print("An exception happened: " + str(err))
