#Nesting: a lits of items inside a dictionary
alien_0 = {'color':'green', 'point':5}
alien_1 = {'color':'yellow', 'point':10}
alien_2 = {'color':'red', 'point':15}

aliens = [alien_0,alien_1,alien_2] # here is where the nesting takes place; a list of dictionaries

#loop through it
for alien in aliens:
 print(alien)

#In reality, lets automate this using range()
#Make an empty list for storing aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30): #how many times this will loop
	new_alien = {'color':'green', 'point':5} # create a new alien
	aliens.append(new_alien) # every new alien created, append to empty dict

#Using a for loop and an if statement to change the color of aliens

for alien in aliens[:3]: #since we only want to change the first 3 aliens we only loop through the slice
	if alien['color'] == 'green': #thsi if statement make sure we only change green aliens to yellow
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

#Show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

#show how many aliens have been created

print(F"Total number of aliens:{len(aliens)}.")
print("\n")

#A list inside a Dictionary(reverse of the example from above)

#

#store information about a pizza being ordered

pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese','pineapple','jalapenos'], #Here is the list[] inside the dictionary {}
	}

# Summarize the order.
print(f"You ordered a {pizza ['crust']} -- crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")

######################################
## You can nest a list inside a dictionary any time you want more than one value to be assosciated with a single key in a dictionary

favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['C'],
	'edward':['ruby','go'],
	'phil':['python','haskell','SQL']
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")