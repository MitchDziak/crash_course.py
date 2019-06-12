pets = []

pet = {
    'name': 'tucker',
    'species': 'dog',
    'age': 12,
    'owner': 'mitch',
    }
pets.append(pet)
    
pet = {
    'name': 'nitro',
    'species': 'bird',
    'age': 1,
    'owner': 'shannon',
    }
pets.append(pet)

pet = {
    'name': 'coco',
    'species': 'cat',
    'age': 2,
    'owner': 'ashton',
    }
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, info in pet.items():
        print("\t" + key.title() + ": " + str(info))
