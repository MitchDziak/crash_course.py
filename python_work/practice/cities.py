cities = {
    'chicago': {
        'country': 'america',
        'population': 1243852,
        'fact': 'immense homicide rates',
        },
    'berlin': {
        'country': 'berlin',
        'population': 2149420,
        'fact': 'great beer',
        },
    'nagasaki': {
        'country': 'japan',
        'population': 0,
        'fact': 'ability to get nuked',
        },
    }

for city, info in cities.items():
    country = info['country'].title()
    population = str(info['population'])
    fact = info['fact']
    
    print("\n + city.title()
