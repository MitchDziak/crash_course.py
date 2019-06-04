animals = ['maned wolf', 'cougar', 'tiger', 'dragon', 'monkey', 'bear']
for animal in animals:
	print(animal)
	print("\nA " + animal + " would make a great pet!")
	print("\n\tA " + animal + " has four legs!")

print("\nI would love to befriend all of these animals.")

for animal in animals:
	animals.pop()
	print(animals)

	
print("Oh no they've all been deleted.")
