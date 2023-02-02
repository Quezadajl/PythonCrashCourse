#Creating a Dictionary from scratch of similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',}

print(favorite_languages)
favorite_languages['phil'] = 'python'
print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

###########################################

#Using get() to Access Values
# alien_no_points.py

alien_0 = {'color': 'green', 'speed':'slow'}
print(alien_0['points'])