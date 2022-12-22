#Hello Admin challenge
usernames = ['totodile','Cyndaquil','Chikorita','Rowlet','Admin']

for username in usernames:
	if usernames == 'Admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello thank you for logging in again.")
	#print("\nFinished making your pizza!!")

not_admin = ['Green','Yellow','Red']
admin = ['admin']
if not_admin in not_admin:
	print('Hello thank you for logging in again.')
if admin == ['admin']:
	print('Hello admin, would you like to see a status report?')