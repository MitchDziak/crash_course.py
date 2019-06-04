names = ['george', 'james', 'edward', 'joseph', 'saul']

print("Hey there, " + names[0].title())
print("Hey there, " + names[1].title())
print("Hey there, " + names[2].title())
print("Hey there, " + names[3].title())
print("Hey there, " + names[-1].title())

cars = ['bmw', 'audi', 'ford']
cars.append('honda')
print(cars)
print("I would like to own a " + cars[0].upper() + " or a " + cars[-1].title())

cars[1] = 'toyota'
print(cars)

cars.append('mazda')
print(cars)

cars.insert(2, 'lincoln')
cars.insert(-2, 'dodge')
print(cars)

del cars[2]
del cars[-2]
print(cars)

popped_car = cars.pop(1)
popped_bmw = cars.pop(0)
print(popped_car.title())
print(popped_bmw.upper())

print(cars)

cars.remove('ford')
print(cars)

cars.append('ford')
cars.append('subaru')
cars.append('bmw')
print(cars)

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(cars)

cars.reverse()
print(cars)
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)

len(cars)
print(len(cars))

cars.append('hyundai')
print(len(cars))

del cars[0]
print(len(cars))

cars.remove('bmw')
print(len(cars))
