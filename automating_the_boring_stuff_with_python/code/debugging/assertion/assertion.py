def assertion():
    ages = [23, 33, 1, 78, 86, 90, 12, 16, 8]
    ages.sort()

    for age in ages:
        print(age)

    assert ages[0] <= ages[-1]
    assert ages[0] == 1

assertion()