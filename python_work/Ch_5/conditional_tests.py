#Creating a list of conditional test to practice: 5-2

snacks = ['peanuts','chocolate','doritos','popcorn']
favorite_snack = 'doritos'

#lets print snacks out, but let everyone know my favorite snack
#for snack in snacks:
#	if snack == favorite_snack:
		#this snack is my favorite, let's let everyone know!
#		print("%s is my favorite snack!" % snack.title()) # -- it looks like the % is used as a variable with additional formating
#	else:
		#I like these other snacks, but not my favorite
#		print("I like %s." % snack)

## other Tests for inequality and equality
#requested_topping = 'pineapple'
#if requested_topping != 'jalapenos':
#	print("Hold the jalapenos!")

needed_ingredients = ['doritos','popcorn','chocolate','fruit'] 
#Here I'm checking if these items are in the pantry
avail_ingredient = 'doritos'

for treat in needed_ingredients:
	if treat == avail_ingredient:
		#this snack is my favorite, let's let everyone know!
		print("Great! we have %s!" % treat.title()) # -- it looks like the % is used as a variable with additional formating
	else:
		#I like these other snacks, but not my favorite
		print("We will need %s from the store." % treat)

#Trying other conditional tests: if-else statements and chains
dogs = ['Dante','Myla','Bunior(cat)']

if len(dogs) >= 4:
	print("Wow, we have a lot of dogs here!")
else:
	print("Okay, this is a reasonable number of dogs.")

#and if-else chains
dogs = ['Sophie','Martin','Lola']#,'Chuying','Guegene']

if len(dogs) >= 5:
	print("Wow,we might start a dog hotel!")
elif len(dogs) >= 3:
	print("wow, we have a lot of dogs here!")
else:
	print("Okay, this is a reasonable number of dogs.")
# if the previous two conditions fail, the else condition is executed; we could keep adding elifs

#of course, using lists and loops can be more clean
#dogs_we_know = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']
#dogs_present = ['willie', 'hootz']
#This will go through all the dogs that are present, and greet the dogs we know
#for dog in dogs_present:
#	if dog in dogs_we_know:
#		print("Hello, %s!" % dog.title())
#True/False statements- The general rule is that any non-zero or non-empty value will evaluate to True
#if -1:
#    print("This evaluates to True.")
#else:
#    print("This evaluates to False.")

# An empty string evaluates to False.
#if '':
#    print("This evaluates to True.")
#else:
#    print("This evaluates to False.")

# Any other string, including a space, evaluates to True.
#if ' ':
#    print("This evaluates to True.")
#else:
#    print("This evaluates to False.")

#Overall Challenge
#alien_names = ['al','lien','ju','andi','ego','uly','ta','pat','Lola','Dante']
#alien_colors = ['red','green', 'blue']