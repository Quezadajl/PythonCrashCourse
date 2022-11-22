banned_users = ['andrew','carolina','david']
user = 'david'
user = 'marie'

if user not in banned_users:
	print(f'{user.title()}, you can post a response if you wish.')
# If teh value user is not in the list banned_users, Python returns True and executes the intended line.