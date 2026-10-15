string = "Hello, World!"

def check_in_string(string, check):
    return check in string

check = ", "

print(check_in_string(string, check)) # Prints True

check = "ldd"

print(check_in_string(string, check)) # Prints false

def check_not_in_string(string, check):
    return check not in string

check = "New"

print(check_not_in_string(string, check)) # Prints True

check = "Hello"

print(check_not_in_string(string, check)) # Prints False