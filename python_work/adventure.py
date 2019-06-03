movement_easy = "You continue on your way to the next encounter."
movement_hard = "After a brutal struggle, you limp away towards the next encounter."
movement_fail = "Your vision dims as you lose all feeling in your body."
enemies_own = ['goblin', 'rat', 'skeleton', 'demon']

print("You're lucky enough to encounter a small " + enemies_own[1] + ", which you dispatch quickly.")
print(movement_easy + "\n")

print("You come across a " + enemies_own[0] + " which poses no threat.")
print(movement_easy + "\n")

print("As you travel through a graveyard, you are spotted by a " + enemies_own[2] + ", \nwhich hastily runs towards you.")
print(movement_hard + "\n")

items = ['Gold: 124', 'dagger', 'mana potion', 'torch', 'stone']

print("You check your inventory.\n")
for item in items[0:]:
    print(item.title())

print("\nYou enter a cave hoping for a brief respite, \nbut you spot a dark shadow emerging from a deep crevice.")
print("It slowly approaches, and as it comes into view, you realize it is a " + enemies_own[-1] + ".")
print("You are gripped with fear, but experience takes control and you rush forward.")
print("You get the first hit in, but the " + enemies_own[-1] + " gets the last.\n")
print(movement_fail)

print("\n\nYour three best items were: " + str(items[:3]))
print("Your three worst items were: " + str(items[-3:]))
print("Your three average items were: " + str(items[1:4]))
