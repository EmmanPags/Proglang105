#Num 1
p1 = {'first_name': 'Jennie', 'last_name': 'Kim', 'age': 22, 'city': 'North Korea'}
p2 = {'first_name': 'Jisoo', 'last_name': 'Kim', 'age': 25, 'city': 'North Korea'}
p3 = {'first_name': 'Lisa', 'last_name': 'Manoban', 'age': 23, 'city': 'Thailand'}

people = [p1, p2, p3]


for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")

#Num 2
pet1 = {'animal': 'Eagle', 'owner': 'Jennie'}
pet2 = {'animal': 'Cat', 'owner': 'Jisoo'}
pet3 = {'animal': 'Gold Fish', 'owner': 'Lisa'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}\n")

#Num 3
favorite_places = {
    'Jennie': ['France', 'Taiwan', 'New Zealand'],
    'Jisoo': ['Hong Kong', 'UAE', 'Greenland'],
    'Lisa': ['Canada', 'Australia']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"  - {place}")
    print()

#Num 4
favorite_numbers = {
    'Jennie': [8, 14, 24],
    'Jisoo': [10, 28, 30],
    'Lisa': [21, 45, 60]
}


for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are: {numbers}\n")

#Num 5
cities = {
    'Taipei': {
        'country': 'Taiwan',
        'population': 2646204,
        'fact': 'It is famous for the Taipei 101 skyscraper.'
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'It is known as the Big Apple.'
    },
    'Jakarta': {
        'country': 'Indonesia',
        'population': 10817400,
        'fact': 'It is the capital city of Indonesia and is known for its vibrant culture.'
    }
}


for city, info in cities.items():
    print(f"City: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
