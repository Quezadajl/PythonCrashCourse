#Practicing if && if-else statements
age = 71
#age = 17
if age >= 18:
	print('You are old enough to vote!')
	print('Have you registered to vote yet?')
else:
	print('Sorry you are too young to vote')
	print('Pleae register to vote when you turn 18!')#All indented lines after an if statement will execute

#Simple conditional tests: if conditional test: do something

#AMUSEMENTPARK.PY
#The if-elif-else Chain
if age <= 4:
	print('admission is free')
elif age <18:
	print('admission is $25')
else:
	print('18 and older pay $40')

#Improved VERSION
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
#elif age >= 65:
	#price = 20 You don't always need an else; not using one causes the last condition to be met as well
else: #else can be misleading by accepting malicious data or invalid statements
	price = 20
print(f'Your admission cost is ${price}.')# improved maintaince by only have to modify one message


#Moral of the practice
block_of_code = ['if','elif']
if'elif' in block_of_code:
	print("if you want only ONE block of code to run, use an if-elif-else chain")
if'if' in block_of_code:
	print('if MORE than one block of code needs to run, use a series of independent if statements')

print('\nThe more you know!\n')

#Alien Colors #5-1 through 5-5
alien_color = ['Green','Yellow','Red']
not_alien = ['Blue']
if 'Green' in alien_color:
	print('5 points')
if 'Yellow' in alien_color:
	print('10 points')
if 'Red' in alien_color:
	print('15 points')
if not_alien != alien_color:
	print('you missed')

#Stages of Life Practice
edad = 29
if edad < 2:
	person = 'baby'
elif edad < 4:
	person = 'toddler'
elif edad < 13:
	person = 'kid'
elif edad < 20:
	person = 'teenager'
elif edad < 65:
	person = 'Adult'
elif edad >= 65:
	person = 'elder'

print(f'Person is a {person}!')

#Favorite Fruit Excercise
favorite_fruits = ['Kiwi','BlueBerries','mango','Bananas']
if 'Kiwi' in favorite_fruits:
	print(f'You really like {favorite_fruits[0]}!')
if 'Bananas' in favorite_fruits:
	print(f'You really like bananas!')
if 'BlueBerries' in favorite_fruits:
	print(f'You really like {favorite_fruits[1]}!')	
if 'Strawberries' in favorite_fruits:
	print(f'You really like Strawberries!')
if 'mango' in favorite_fruits:
	print(f'You really like {favorite_fruits[-2]}!')

#Testing Multiple conditions AND ALL of them have to pass!!: TOPPINGS.PY
requested_toppings = ['mushrooms','green peppers','extra cheese']
#if 'mushrooms' in requested_toppings:
	#print('Adding mushrooms.')
#if 'pepperoni' in requested_toppings:
	#print('Adding pepperoni.')
#if 'extra cheese' in requested_toppings:
	#print('Adding extra cheese.')

#print("\nFinished making your pizza!")*/

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")