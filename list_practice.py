#Step 2: Creating a list
cities = [
    'Oakland',
    'Atlanta',
    'New York City',
    'Seattle',
    'Memphis',
    'Miami',
    'Boston',
    'Los Angeles',
    'Denver',
    'New Orleans',
]

print(cities)

#Step 3: Creating your own list and printing from a list
pc_parts = [
    'CPU',
    'GPU',
    'Motherboard',
    'RAM',
    'SSD',
    'CPU Cooler',
    'PSU',
    'Fans',
    'CPU Cooler',
]

print()
print(cities[1])
print(cities[0])
print(cities[-1])

#Step 4: List slicing
three_cities = cities[0:4]
three_pc_parts = pc_parts[0:4]

print()
print(three_cities)
print(three_pc_parts)