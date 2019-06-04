age = -5

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
else:
    price = 'ERROR'
    
print("Your admission cost is $" + str(price) + ".")

money = 5

if money < 5:
    admission = 'You do not have enough money'
elif money == 5:
    admission = 'You have just enough money'
else:
    admission = 'You have enough money and some to spare'
    
print(admission + ", $" + str(price))
