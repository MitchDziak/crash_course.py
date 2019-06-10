# Initial dictionary of people and their favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_takers = ['ashton', 'shannon', 'wiese', 'mitch', 'jen', 'phil']

for poll_taker in poll_takers:
    if poll_taker not in favorite_languages.keys():
        print("You need to take the poll, " + poll_taker.title() + ".")
    else:
        print("Thanks for taking the poll, " + poll_taker.title() + ".")
print("\n")
    

# Prints a statement about the favorite language of specific keys in a list
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print("  Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
  
# Thanks each participant for the poll, asks non-participants to take it.
print("\n")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


