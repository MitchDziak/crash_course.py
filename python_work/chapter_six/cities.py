cities = {
    'chicago': {
        'country': 'United States',
        'population': 2716000,
        'fact': 'infamous for homicide',
        },
    'hiroshima': {
        'country': 'japan',
        'population': 1194000,
        'fact': 'known for okonomiyaki',
        },
    'berlin': {
        'country': 'germany',
        'population': 3575000,
        'fact': 'famous for beer',
        },
    }
    
for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact']
    
    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of " + str(population) + ".")
    print("  This city is " + fact)
