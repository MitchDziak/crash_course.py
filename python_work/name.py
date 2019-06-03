# This was a test to see what I could do with titlecase, uppercase, and lowercase

name = "mitch dziak"
first_name = "mitch"
last_name = "dziak"
print(name.title())
print(name.upper())
print(name.lower())
print(first_name.upper() + " " + last_name.lower())
print(first_name.lower() + " " + last_name.upper())

print("\t\t\t\t:)")

# Here I wanted to see how tabs and new lines worked when included in a string.
# It looks like you have to put \t AFTER \n to start with a tab, which makes sense.


message = "\tGreetings, " + name.title() + "!"
print(message)
print("\n\n")
print("I\nhope\n\tyou\n\tare\nhaving\nan\n\tamazing\nday!")

xy = "man"
xx = "woman"

current_language = 'english '
print(current_language + xy)
print(current_language.rstrip() + xy)
print("")
print(current_language + xx)
current_language = current_language.rstrip()
print(current_language + xx)
