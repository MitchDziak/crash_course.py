people = []

person = {
    'first name': 'ashton',
    'age': 21,
    'last name': 'wood-knife',
    'city': 'seattle',
    }
people.append(person)
    
person = {
    'first name': 'cameron',
    'age': 27,
    'last name': 'dziak',
    'city': 'homer glen',
    }
people.append(person)

person = {
    'first name': 'shannon',
    'age': 22,
    'last name': 'drage',
    'city': 'geneva',
    }
people.append(person)

for person in people:
    first = person['first name'].title()
    last = person['last name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(first + " " + last + " lives in " + city + " and is " + age +".")
