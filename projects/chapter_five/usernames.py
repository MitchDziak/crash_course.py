current_users = ['rusatus', 'koutavi', 'rainydaysmell', 'coalhustler', 'admin']

new_users = ['ashton', 'wiese', 'KOUTAVI', 'Rusatus', 'AdMiN', 'rainydaysmell']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Username already taken. Please choose another.")
	else:
		print("That username is available!")
