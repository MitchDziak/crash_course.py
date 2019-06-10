usernames = ['popcorn', 'coalhustler', 'koutavi', 'rusatus', 'admin']

if usernames:
    for username in usernames:
	    if username == 'admin':
	    	print("Welcome " + username + ", would you like to see status report?")
	    else:
		    print("Hello " + username + ", thank you for logging in again.")
else:
	print("We need to find some users!")
