banned_users = ['andrew','carolina','david']
user = 'david'
#user = 'marie'

if user not in banned_users:
	print(f'{user.title()}, you can post a response if you wish.')
# If teh value user is not in the list banned_users, Python returns True and executes the intended line.

#Coditional Test 5-1
#car = 'Subaru'
#print("is car == 'subaru'? I predict True.")
#print(car == 'subaru') # Case is important with conditional tests, hence why it's false if lower case
#print("\nIs car == 'audi'? I predict False")
#print(car == 'audi')