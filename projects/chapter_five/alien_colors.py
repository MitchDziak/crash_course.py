alien_color = ['red']

if 'green' in alien_color:
	print("5 points earned!")
if 'red' in alien_color:
	print("5 points earned!")
	
alien_color.append('purple')

if 'green' in alien_color:
	print("5 points earned!")
elif 'purple' in alien_color:
	print("10 points earned!")
else:
	print("You've found a glitch!")
	
if 'blue' in alien_color:
	print("5 points earned!")
else:
	print("That alien wasn't blue!")

alien_color.append('yellow')

if 'green' in alien_color:
	print("5 points earned!")
elif 'yellow' in alien_color:
	print("10 points earned!")
elif 'red' in alien_color:
	print("15 points earned!")
else:
	print("What the hell?")
	

