# Page 112 version of favorite_languages.py

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())



# # Initial dictionary of people and their favorite languages
# favorite_languages = {
    # 'jen': 'python',
    # 'sarah': 'c',
    # 'edward': 'ruby',
    # 'phil': 'python',
    # }

# # 

# # Prints only a list of the key values omitting keys using .values()
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
    # print("\t" + language.title())

# # Prints a statement about the favorite language of specific keys in a list
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
    # print(name.title())
    
    # if name in friends:
        # print("  Hi " + name.title() +
            # ", I see your favorite language is " +
            # favorite_languages[name].title() + "!")
  
# # Thanks each participant for the poll, asks non-participants to take it.
# print("\n")
# for name in sorted(favorite_languages.keys()):
    # print(name.title() + ", thank you for taking the poll.")
# if 'erin' not in favorite_languages.keys():
    # print("Erin, please take our poll!")
