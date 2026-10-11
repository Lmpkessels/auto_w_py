birthdays = {}

print("Please provide your name: ")
name = input()
print("Please provide your birthday: ")
birthday = input()

birthdays[name] = birthday

print(birthdays)

def incr_dict(dicti, x, y):
    dicti[x] = y

dicti = {}
incr_dict(dicti, 'Name', 'Luuk')
print(dicti)