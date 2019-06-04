users = ['Cooldude', 'ranch', 'squip', 'faze_gunk']
banned_users = ['ur_mom', 'Ninja', 'RUSATUS', 'cooldude']

if users[0].lower() == 'cooldude':
    print(users[0] + " is a user.")

age_0 = 20
age_1 = 21
age_2 = 25
age_3 = 64

if age_0 <= 21:
    print("User is not 21+")
    
if age_2 >= 21:
    print("User is 21+")
    
if age_0 or age_3 == 64:
    print("One user is old af.")
    
if age_0 or age_2 != 24:
    print("Neither user is 24.")

if users[0].lower() not in banned_users:
    print(users[0] + " is not banned.")
else:
    print(users[0] + " is banned.")
    
for user in users:
    if user == 'cooldude':
        print(user + " is banned.")
    else:
        print(user + " is not banned.")
