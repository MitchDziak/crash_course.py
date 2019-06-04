count = list(range(1,1000001))
print(count)

print(min(count))
print(max(count))
print(sum(count))

odd = list(range(1,21,2))
print(odd)

odds = []
for value in range(1,21):
	odds.append(value*2)
print(odds)
	

multiples = []
for value in range(1,31):
	multiples.append(value*3)
print(multiples)

cubes = []
for value in range(1,10):
	cubes.append(value**3)
print(cubes)

cubes = [value**3 for value in range(1,10)]
print(cubes)
