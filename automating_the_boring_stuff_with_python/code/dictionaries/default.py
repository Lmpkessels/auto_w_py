car = {
    'Car': 'Renault',
    'Type': 'Twingo',
}

COLOR = 'Color'

# Manually checking
if COLOR not in car:
    car[COLOR] = 'Black'

print(car)

car = {
    'Car': 'Audi',
    'Type': 'A3',
}

# Instead of setting it up manually
car.setdefault(COLOR, 'Black')

print(car)