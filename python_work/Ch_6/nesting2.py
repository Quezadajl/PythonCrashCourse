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
#for username, user_info in users.items(): # we loop through the user's info
#	print(f"\nUsername: {username}") # print the username info
#	full_name = f"{user_info['first']} {user_info['last']}" # accessing inner dict, the last three keys
#	location = user_info['location'] # print summary

#	print(f"\tFull name: {full_name.title()}")
#	print(f"\tLocation: {location.title()}")

## 6.7 People
#Start with the program you wrote for Exercise 6-1 (page 102).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you
#loop through the list, print everything you know about each person.

person_0 = {
	'first_name': 'J',
	'last_name': 'D',
	'age': 29,
	'city': 'Talmo'
}

person_1 = {
	'first_name': 'Dwight',
	'last_name': 'Shrute',
	'age': 33,
	'city': 'Talmo'
}

person_2 = {
	'first_name': 'Jim',
	'last_name': 'Howard',
	'age': 27,
	'city': 'Jefferson'
}

#persons = [person_0, person_1, person_2]

#for person in persons:
#	print(person)

## 6.8 Pets
#Make several dictionaries, where the name of each dictionary is the
#name of a pet. In each dictionary, include the kind of animal and the owner’s
#name. Store these dictionaries in a list called pets. Next, loop through your list
#and as you do print everything you know about each pet.

Martin = {
	'species': 'Mix Lab',
	'color': 'black/gold',
	'owner': 'Joselit',
}
Sophie = {
	'species': 'Chihuahua',
	'color': 'brown',
	'owner': 'Ojitos',
}
Lola = {
	'species': 'Hairy mix',
	'color': 'Oreo',
	'owner': 'Joselit',
}

pets = [Martin, Sophie, Lola]

#for pet in pets:
#	print(pet)

## 6.9 Favorite Places
#Make a dictionary called favorite_places. Think of three
#names to use as keys in the dictionary, and store one to three favorite places
#for each person. To make this exercise a bit more interesting, ask some friends
#to name a few of their favorite places. Loop through the dictionary, and print
#each person’s name and their favorite places.

favorite_places = {
	'Joselit': ['Beach', 'Rome', 'Harpeth River'],
	'Tania': ['Rome', 'Paris', 'New York'],
	'Martin': ['home', 'couch', 'park'],
}

#for name, places in favorite_places.items():
#	print(name.title() + ", your favorite places are:")
#	for place in places:
#		print("\t" + place.title())
