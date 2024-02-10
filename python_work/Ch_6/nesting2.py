#DictionaryInADictionary
users = {
	'aeinstein' : {
	'first':'albert',
	'last':'einstein',
	'location':'princeton',
	},

	'mcurie': {
	'first':'marie',
	'last':'curie',
	'location':'paris',
	},
}
# we define a dict with 2 keys, each key is a dict with user info
for username, user_info in users.items(): # we loop through the user's info
	print(f"\nUsername: {username}") # print the username info
	full_name = f"{user_info['first']} {user_info['last']}" # accessing inner dict, the last three keys
	location = user_info['location'] # print summary

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")