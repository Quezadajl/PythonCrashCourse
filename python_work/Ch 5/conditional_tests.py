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

needed_ingredients = ['doritos','popcorn','chocolate','fruit'] #Here I'm checking if these items are in the pantry
avail_ingredient = 'chocolate'

for treat in needed_ingredients:
	if treat == avail_ingredient:
		#this snack is my favorite, let's let everyone know!
		print("Great we have %s!" % treat.title()) # -- it looks like the % is used as a variable with additional formating
	else:
		#I like these other snacks, but not my favorite
		print("We will need %s from the store." % treat)

#Trying other conditional tests: if-else statements
dogs = ['Sophie','Martin','Lola']

if len(dogs) > 3:
	print("Wow, we have a lot of dogs here!")
else:
	print("Okay, this is a reasonable number of dogs.")