msg = "Welcome to my practice program! Get ready for a wild ride!"
print(msg)

# 2-3 through 2-7 Try It Yourself's
user = "mitch"

print("\nHello, " + user.title() + " do you remember what you learned?")
print(user.title())
print(user.lower())
print(user.upper())

print('\nThe wise guru, ' + user.title() + ', once said, "Bruh," right before leaping off of a cliff.')
quote = '\nThe great one, ' + user.title() + ', was never heard from again, except for a mysterious letter that appeared at his old home. The message only said one word: "Gottem"'
print(quote)

print(user.lstrip())
print(user.rstrip())
print(user.strip())

numbers = list(range(1,11,2))
print(numbers)

cubes = [value**3 for value in range(1,11)]
print(cubes)


bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[0].title())
print(bicycles[-1].upper())
bicycle_message = "My first bike was a " + bicycles[0].title() + "."
print(bicycle_message)

names = ['sam', 'mitch', 'shannon', 'cam']

print(names[0])
print(names[3].title())
print("Hello, " + names[-1].title() + ".")
names_message = "How are you, " + names[2].upper() + "?"
print(names_message)
