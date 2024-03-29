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
print(person_0['city'])
print(person_0)

## 6.2
#Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.

fav_numbers = {
	'Martin': 10,
	'Lola': 2,
	'Sophie': 12,
	'sookie': 100,
	'elsa':1,
}

#print("Martin's favorite number is " + str(fav_numbers['Martin']))
#print("Sophie's favorite number is " + str(fav_numbers['Sophie']))

##########################################

## 6.3
#A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.
	#Print each word and its meaning as neatly formatted output. You might
	#print the word followed by a colon and then its meaning, or print the word
	#on one line and then print its meaning indented on a second line. Use the
	#newline character (\n) to insert a blank line between each word-meaning
	#pair in your output.

glossary = {
	'concatenate': 'to join two strings or other applicable object ' +
		'types together.',
	'for loops': 'for loops are used to perform some action on each ' +
		'item in a list.',
	'lists': 'lists are used to store multiple objects together',
	'if-elif-else': 'if-elif-else statements can be used to evaluate ' +
		'if an element meets certain criteria and executes blocks of ' +
		'code based on which (if any) of these criteria are met.',
}
#print('concatenate :')
#print(glossary['concatenate'] + '\n')
#print('for loops :')
#print(glossary['for loops'])

###########################################
## 6.4
#Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.

for word, definition in glossary.items():
	print(word + " :\n" + definition + '\n')

###########################################

## 6.5
#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.
#• Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#• Use a loop to print the name of each river included in the dictionary.
#• Use a loop to print the name of each country included in the dictionary.

rivers = {
	'mississippi': 'the united states',
	'nile': 'egypt',
	'amazon': 'brazil',
	'harpeth':'Franklin',
	'Cumberland':'Nashville'
}

for river, country in rivers.items():
	print("The " + river.title() + " river runs through " + country.title() + ".")
print('\n')
for river in rivers.keys():
	print(river)
print('\n')
for country in rivers.values():
	print(country)

#########################################

## 6.6 Polling. Use the code in favorite_languages.py (page 104)
#• Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#• Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

poll_list = ['edward', 'allie', 'william', 'sarah', 'luke']

for name in poll_list:
	if name in favorite_languages.keys():
		print(name.title() + ", thank you for taking the favorite languages poll.")
	else:
		print(name.title() + ", please go take the poll.")

###########################################


#Using get() to Access Values
# alien_no_points.py

alien_0 = {
	#'color': 'green', 
	'speed':'slow', 
	#'points':0,
	}
#Working around the traceback error especifically for this, we have used the get method to bypass it
#The get() method requires a key for first argument, and an optional second argument to return a value..
#..if first argument is null
point_value = alien_0.get('points','No point value assigned.')
print(point_value)

color_get = alien_0.get('color', 'No color value assigned')
print(color_get)

#print(alien_0['color'])	