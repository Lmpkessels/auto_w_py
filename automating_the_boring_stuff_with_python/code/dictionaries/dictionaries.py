user = {
    'name': 'Luuk',
    'lastname': 'Kessels',
    'middle name': 'Martinus Petrus',
    'age': '26',
}

user_name = user['name']

for k, v in user.items():
    print("Key: " + k, "|", "Value: " + v)

print("Please provide your name: ")
i_usr_name = input()

for k, v in user.items():
    if v == i_usr_name:
        print(f"Hello, {i_usr_name}!")

print(user_name)