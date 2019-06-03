pizzas = ['pepperoni', 'sausage', 'cheese']

friend_pizzas = pizzas[:]

friend_pizzas.append('vegan')

pizzas.append('bacon')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
    

print("\nPizza is great!")

