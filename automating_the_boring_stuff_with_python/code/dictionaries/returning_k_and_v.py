def get_keys(dicti):
    for k in dicti.keys():
        print(k)

def get_values(dicti):
    for v in dicti.values():
        print(v)

def get_keys_and_values(dicti):
    for k, v in dicti.items():
        print(k + ':', v)

def search_key(dicti, key):
    if key in dicti:
        return True
    
    return False

def search_value(dicti, value):
    if value in dicti:
        return True
    
    return False

MISSING = object()

def check_existence(dicti, key):
    value = dicti.get(key, MISSING)

    if value == MISSING:
        print("Key does not exist")
    else:
        print(value)

dicti = {
    'Name': 'Luuk',
    'Lastname': 'Kessels',
    'Holy names': 'Martinus Petrus',
    'Age': '26',
    'Birthday': '2000-23-02'
}

get_keys(dicti)
get_values(dicti)
get_keys_and_values(dicti)

print(search_key(dicti, 'Name'))
print(search_value(dicti, 'Koen'))