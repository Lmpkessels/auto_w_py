def greet_user():
    print("Provide your name: ")
    name = input()

    if not name.isalpha():
        raise Exception("name must be of characters")

try:
    greet_user()
except Exception as err:
    print("An exception happened: " + str(err))