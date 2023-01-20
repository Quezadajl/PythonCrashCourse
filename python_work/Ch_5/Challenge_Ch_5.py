#Hello Admin challenge
usernames = ['totodile','Cyndaquil','Chikorita','Rowlet','Admin','Chimpchar']
root_user = ['Admin']
usernames = []
if 'totodile' in usernames:
	print(f'Hello! thank you for logging in again.')
if 'Cyndaquil' in usernames:
	print(f'Hello!, thank you for logging in again.')
if 'Rowlet' in usernames:
	print(f'Hello! thank you for logging in again.')
if 'Chimpchar' in usernames:
	print(f'Hello!, thank you for logging in again')
if 'Admin' in usernames:
	print('Hello admin, would you like to see a status report?')
if usernames is []:
	print('We need to find some users!')

for root in root_user:
	if root in usernames:
		print('Hello Admin, would you like to see the status of the report')
	#if root not in usernames:
		#print('Hello! thank you for logging in again')
	else:
		print('We need to find some users!')

current_users = ['Mario','Luigi','luigi','Pricess Peach','Toad','Yoshi']
new_users = ['Mario','luigi','Princess Daisy', 'Rosalina','yoshi']

for new_user in new_users:
	if new_user.title() in current_users:
		print(new_user,'is NOT available, must enter an new username')
	else:
		print(new_user, 'is available')
