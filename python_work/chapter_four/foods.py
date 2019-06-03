my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy Friend's favorite foods are:")
print(friend_foods)

print("\n")
for my_food in my_foods:
    print("I want to eat " + my_food)
    
print("\n")
for friend_food in friend_foods:
    print("My friend wants to eat " + friend_food)

