#Hello Admin challenge
usernames = ['totodile','Cyndaquil','Chikorita','Rowlet','Admin']
if usernames:
	for username in usernames:
		if usernames == 'Admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello thank you for logging in again.")
	#print("\nFinished making your pizza!!")
else:
	print("Did the email send?")