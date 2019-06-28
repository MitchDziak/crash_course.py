def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nMy pet is a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('cat', 'guthix')
describe_pet(animal_type='parakeet', pet_name='nitro')

