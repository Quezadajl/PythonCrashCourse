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

#favorite_languages = {
#	'jen': 'python',
#	'sarah': 'c',
#	'edward': 'ruby',}

#print(favorite_languages)
#favorite_languages['phil'] = 'python'
#print(favorite_languages)

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")

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

#color_get = alien_0.get('color', 'No color value assigned')
#print(color_get)

#print(favorite_games['juandiego']) #print person's fav game
	