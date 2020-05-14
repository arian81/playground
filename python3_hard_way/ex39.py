states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

Cities['NY'] = 'New York'
Cities['OR'] = 'Portland'

print('_' * 10)
print("NY State has: ", Cities['NY'])
print("OR State has: ", Cities['OR'])

print('_' * 10)
print("Michigan's abbrevation is ", states['Michigan'])
print("Florida's abbrevation is ", states['Florida'])

print ('_' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has : ", cities[states['Florida']])

print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('_' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abrev} has the city {city}")

print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_' * 10)
state = states.get("Texas")

if not state:
    print("sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
