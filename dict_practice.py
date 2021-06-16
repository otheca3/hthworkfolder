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