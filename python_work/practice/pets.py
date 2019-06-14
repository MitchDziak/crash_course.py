pets = []

pet = {
    'name': 'tucker',
    'owner': 'mitch',
    'age': 12,
    'favorite toy': 'shoes',
    }
pets.append(pet)

pet = {
    'name': 'oliver',
    'owner': 'shannon',
    'age': 3,
    'favorite toy': 'gatorade bottles',
    }
pets.append(pet)

pet = {
    'name': 'coco',
    'owner': 'ashton',
    'age': 4,
    'favorite toy': 'yarn',
    }
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about" + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))

for pet in pets:
    name = pet['name'].title()
    owner = pet['owner'].title()
    age = str(pet['age'])
    toy = pet['favorite toy']
    
    print("This is " + owner + "'s pet " + name + ".\n" +
    "He is " + age + " years old.\nHis favorite toy is " + toy + "\n")

