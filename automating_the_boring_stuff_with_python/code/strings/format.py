# Formating strings
name = "Luuk"
formated = f"This is a formated string with the name: {name}, using 'f'"
print(formated)

formated = "This is a fromated string with the name: {}, using format()".format(name)
print(formated)

# Greets user by first name
def greet_user():
    true = True

    print("Enter your firstname: ")
    while true:
        name = input()
        
        if not name.isalpha():
            print("Please only use characters")
            continue
        else:
            true = False

    print(f"Hello, {name}!")

greet_user()