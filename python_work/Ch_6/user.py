user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'femi'
}

#Using  a for loop in a dictionary

for key, value in user_0.items(): #include the name of a dictionary followed by method items()
	print(f"\nKey:{key}")
	print(f"Value:{value}")

#use abbreviations too
for k,v in user_0.items():
	print(f"\nKey:{key}")
	print(f"Value:{value}")
###################################
#Practicing using the data from favorite_languages tab

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',}

print(favorite_languages)
favorite_languages['phil'] = 'python'
print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"\n\tSarah's favorite language is {language}.")

for name, language in favorite_languages.items():
	print(f"\n{name.title()}'s favorite language is {language.title()}")


##########################################
#Looping through the keys in a dictionary

for name in favorite_languages.keys():  # Using the keys() method
	print(name.title())

for name in favorite_languages:  #printing keys is the default behavior w/o the method keys()
	print(name.title())