#Hello Admin challenge
usernames = ['totodile','Cyndaquil','Chikorita','Rowlet','Admin','Chimpchar']
root_user = ['Admin']

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

for root in root_user:
	if root in usernames:
		print('Hello Admin, would you like to see the status of the report')
	if root not in usernames:
		print('Hello! thank you for logging in again')
	else:
		print('Hello! thank you for logging in again')