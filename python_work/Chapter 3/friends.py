names = ['val', 'sean', ' Ashton ', 'Wiese ', ' Shannon']
print(names[0].title())
print(names[1].title())
print(names[-3].strip())
print(names[-2].rstrip())
print(names[4].lstrip())

print("\n\nHow is your day, " + names[0].title() + "?")
print("How is your day, " + names[1].title() + "?")
print("How is your day, " + names[2].strip() + "?")
print("How is your day, " + names[3].rstrip() + "?")
print("How is your day, " + names[4].lstrip() + "?")

transport = ['bmw', 'honda civic', 'Bicycle', ' horse', ' sandwich ']

print("\n\nI would love to fix my " + transport[0].upper() + ".")
print("I would rather own a " + transport[1].title()+ ".")
print("I want to ride my " + transport[2].lower() + ".")
print("I cannot easily ride a " + transport[3].lstrip() + ".")
print("There is nothing better than a " + transport[-1].strip() + ".")
