rivers = {
    'nile': 'egypt',
    'fox': 'illinois',
    'amazon': 'brazil'
    }

for k, v in rivers.items():
    print("The " + k.title() + " river runs through " + v.title())

for k in rivers.keys():
    print(k)

for v in rivers.values():
    print(v)
