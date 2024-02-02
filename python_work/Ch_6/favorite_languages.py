#Creating a Dictionary from scratch of similar objects
#favorite_games = {
#	'juandiego': 'Yakuza',
#	'Ulysses':'Fortnite',
#	'Paty':'Phase 10',
#	'Linda':'Marble Game',
#}
#print(favorite_games)
#favorite_games['Luisito'] = 'pokemon'
#print(favorite_games)
#game = favorite_games['Luisito'].title()
#game1 = favorite_games['juandiego'].title()
#print(f"Luisito's favorite game is {game}.\n")
#print(f"juandiego's favorite game is {game1}.\n")


#for key, value in favorite_games.items(): #include the name of a dictionary followed by method items()
#	print(f"\nKey:{key}")
#	print(f"Value:{value}")

#########################################

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',}

#print(favorite_languages)
favorite_languages['phil'] = 'python'
#print(favorite_languages)

language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")

#if 'erin' not in favorite_languages.keys():
	#print("Erin, please take our poll!")

#for name in sorted(favorite_languages.keys()):
	#print(f"{name.title()}, thank you for taking the poll.")
###### Looping through All values in a Dictionary ####
#print("The following languages have been mentioned:")
#for language in favorite_languages.values():
	#print(language.title())

##### Using Set() will only pull the UNIQUE values from a dictionary###

#print("The following UNIQUE languages have been mentioned:")
#for language in set(favorite_languages.values()):
	#print(language.title())

####-----#####	

## 6.1
#Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

person_0 = {
	'first_name': 'Jose',
	'last_name': 'Quezada',
	'age': 30,
	'city': 'Franklin'
}
print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
#print(person_0['city'])
#print(person_0)

###########################################

#Using get() to Access Values
# alien_no_points.py

alien_0 = {
	'color': 'green', 
	'speed':'slow', 
	'points':0,
	}
#Working around the traceback error especifically for this, we have used the get method to bypass it
#The get() method requires a key for first argument, and an optional second argument to return a value..
#..if first argument is null
point_value = alien_0.get('points','No point value assigned.')
print(point_value)

color_get = alien_0.get('color', 'No color value assigned')
print(color_get)
	