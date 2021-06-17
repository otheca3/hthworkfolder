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

#Step 5: Changing elements in a list

cities[0] = 'San Francisco'
cities[2] = 'Brooklyn'
cities[-3] = 'Hollywood'
cities[5] = 'Tampa'

#Step 6: Adding things to a list
cities.append('Oakland')
cities.extend(['New York City', 'Los Angeles'])
cities.insert(0, 'Miami')

#Step 7: Deleting elements from a list
del cities[1]
cities.pop(3)
cities.remove('Tampa')


def check_list(list1):
    for element in list1:
        print(element)

    return 'Done'

check_list(cities)

#not finished, kind of confused
'''
def word_length_sort(list1):
    temp_dict = {}
    for i in range(len(list1)):
        temp_dict[i] = len(list1[i])
    
    return temp_dict

print()
print(word_length_sort(cities))
'''