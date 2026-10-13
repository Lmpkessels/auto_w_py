ARROW = 'Arrow'
GOLD_COIN = 'Gold coin'
BOW = 'Bow'
ARMOUR_PLATE = 'Armour plate'
WEED = 'Weed'

loot = [ARROW, WEED, WEED, ARMOUR_PLATE, BOW, ARROW, GOLD_COIN, GOLD_COIN, WEED]
inventory = {}

def add_item(inventory, loot):
    for item in loot:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory

def view_inventory(inventory):
    total_i = 0

    print('Inventory:')
    for k, v in inventory.items():
        total_i += v
        print(str(v) + ':', k)

    print("The total number of items is: " + str(total_i))

add_item(inventory, loot)
view_inventory(inventory)