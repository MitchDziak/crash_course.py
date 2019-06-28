locations = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Where would you like to go for your dream vacation? ")
    
    locations[name] = response
    
    repeat = input("Would you like somebody else to respond? (yes/ no) ")
    if repeat == 'no' or 'No' or 'N' or 'n':
        polling_active = False
    
        
for name, response in locations.items():
    print(name + " would like to visit " + response + ".")
