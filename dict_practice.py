#Step 2: Creating a dictionary
meat_products = {
    'Chicken' : 1.59,
    'Beef' : 1.99, 
    'Cheese' : 1.00, 
    'Milk' : 2.50,
}

#Step 3: Creating my own dictionary
valorant_agents = {
    'Controller' : 'Viper',
    'Duelist' : 'Reyna',
    'Sentinal' : 'Cypher',
    'Initiator' : 'Breach',
}

#Step 4: Accessing the values in a dictionary
print(meat_products['Chicken'])
print(meat_products['Beef'])

#Step 5: Changing Values in a dictionary
print()
print(valorant_agents['Controller'])
print(valorant_agents['Sentinal'])

valorant_agents['Controller'] = 'Omen'
valorant_agents['Sentinal'] = 'Sage'

print()
print(valorant_agents['Controller'])
print(valorant_agents['Sentinal'])

#Step 6: Another dictionary
inventory = {
    'Jordan 13' : 1,
    'Yeezy' : 8,
    'Foamposite' : 10,
    'Air Max' : 5,
    'SB Dunk' : 20,
}

#Step 7: Updating Inventory
inventory['SB Dunk'] -= 2
inventory['Yeezy'] += 1
for key in inventory:
    inventory[key] += 7
    inventory[key] -= 3

print()
print(inventory)

#Step 8: Adding new values to dictionaries
inventory['Vans'] = 10
inventory['Converse'] = 7
inventory['Sketchers'] = 0

#Step 9: Deleting values in a dictionary
del inventory['Yeezy']
del inventory['Foamposite']

print()
print(inventory)


#Lab 4 Stuff
def total_price(item1, item2):
    price1 = meat_products[item1]
    price2 = meat_products[item2]

    total = price1 + price2
    return total

beef_cheese_price = total_price('Beef', 'Cheese')
print()
print(beef_cheese_price)

def price_difference(item1, item2):
    price1 = meat_products[item1]
    price2 = meat_products[item2]

    price_diff = abs(price1 - price2)
    return price_diff

beef_cheese_diff = price_difference('Beef', 'Cheese')
print()
print(beef_cheese_diff)

def restock(item, multiplier):
    old_stock = inventory[item]
    new_stock = old_stock * multiplier

    inventory[item] = new_stock
    return inventory

print()
print(restock('Vans', 3))

def clearance(item, divider):
    old_stock = inventory[item]
    new_stock = old_stock // divider

    inventory[item] = new_stock
    return inventory

print()
print(clearance('SB Dunk', 3))

bugs_in_my_house = {
    'fly' : 10,
    'roach' : 0,
    'crickets' : 1,
    'me' : 1,
}

def update_bugs(bug, num):
    bugs_in_my_house[bug] += num
    return bugs_in_my_house

print()
print(update_bugs('me', 3))