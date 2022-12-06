#Creating a list of conditional test to practice: 5-2

snacks = ['peanuts','chocolate','doritos','popcorn']
favorite_snack = 'doritos'

#lets print snacks out, but let everyone know my favorite snack
for snack in snacks:
	if snack == favorite_snack:
		#this snack is my favorite, let's let everyone know!
		print("%s is my favorite snack!" % snack.title()) # -- it looks like the % is used as a variable with additional formating
	else:
		#I like these other snacks, but not my favorite
		print("I like %s." % snack)

## other Tests for inequality and equality
requested_topping = 'pineapple'
if requested_topping != 'jalapenos':
	print("Hold the jalapenos!")

requested_snacks = ['doritos'or'popcorn'or'chocolate'] #Here I'm checking if these items are in the pantry
for treat in requested_snacks:
	if requested_snacks == 'Fruit': #These are the only registered items in my list
		print(f'Google add {requested_snacks} to shopping list!')#make request to add to shopping list if missing or low
	else:
		print(f"I'll take some {requested_snacks[0]}!")