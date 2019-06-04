# This is the initial list of guests
guests = ['george', 'james', 'brian', 'shannon']

# This prints a statement regarding the first guest
print("Would you like to come to dinner, " + guests[0].title() + "?")
print(guests)

# This pops the last guest and prints the value
guest_popped = guests.pop(-1)
print(guest_popped)
print(guests)

# This inserts a new guest in the middle of the list, prints it.
guests.insert(3, 'cam')
print(guests)
print("Come on by, " + guests[-1].title() + ".")

# This inserts two more guests, one at the beginning and middle, and appends one at the end
guests.insert(0, 'butt')
guests.insert(1, 'gunk')
guests.append('poo')

print(guests)

print("We are inviting " + str(len(guests)) + " guests to the occasion.")

# This pops every guest but the last two, printing a message for each.
print("Sorry, we can only invite two guests.")
first_popped = guests.pop()
print("You're out, " + first_popped)
second_popped = guests.pop()
print("You're out, " + second_popped)
third_popped = guests.pop()
print("You're out, " + third_popped)
fourth_popped = guests.pop()
print("You're out, " + fourth_popped)
fifth_popped = guests.pop()
print("You're out, " + fifth_popped)
print("\n\n")

# This prints the last two guests.
print("Welcome, " + guests[0].title() + ".")
print("Welcome, " + guests[1].title() + ".")

# This deletes the remaining two values in the list, prints it to confirm.
del guests[1]
del guests[0]
print(guests)

