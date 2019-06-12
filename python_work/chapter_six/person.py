people = []

person = {
    'first name': 'fred',
    'last name': 'argentine',
    'age': 24,
    'city': 'argentina',
    }
people.append(person)

person = {
    'first name': 'mitch',
    'last name': 'dziak',
    'age': 22,
    'city': 'homer glen',
    }
people.append(person)

person = {
    'first name': 'shannon',
    'last name': 'drage',
    'age': 22,
    'city': 'geneva',
    }
people.append(person)

for person in people:
    name = person['first name'].title() + " " + person['last name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + " is from " + city + " and is " + age + " years old.")
