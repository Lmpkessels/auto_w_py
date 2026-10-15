def check_char(char):
    if char.isalpha():
        print(f"Char contains the alpha letters: {char}")
    elif char.isalnum():
        print(f"Char contains the numbers: {char}")
    elif char.isdecimal():
        print(f"Char contains the decimal: {char}")
    elif char.isspace():
        print(f"Char contains a space")
    elif char.istitle():
        print(f"Char contains the title: {char}")
    else:
        print("Not alpha, numbers, decimal, space, or title")

alpha = "abcdefg"
alnum = "123456"
decimal = "12121"
space = " "
title = "Programming Bitcoin"

check_char(alpha)
check_char(alnum)
check_char(decimal)
check_char(space)
check_char(title)