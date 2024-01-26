#Intro to if statements in python
cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':#if the value of car is 'bmw' upper case
		print(car.upper())
	else:
		print(car.title())#otherwise the value of car is anthing othar than 'bmw', title case it

#Practice
doggos = ['Paper','chuying/Eugene','Rock','Scissors']

for good_dog in doggos:
	if good_dog =='chuying/Eugene':
		print(good_dog.title())
	else:
		print(f'\nBestest of Doggos!!')

#Conditional statements
auto = ['Audi']

for vehicle in auto:
	if vehicle == 'Audi':
		print(True)
	else:
		print(False)


#for vehicle in auto:
#	if vehicle == 'audi':
#		print(True)
#	else:
#		print(False)

#next_section= print(f'\nChecking for inequalities: Next Section\n')#toppings.py

#requested_topping = 'mushrooms' 

#if requested_topping != 'anchovies': #This line compares the value or requested_topping ot the value 'anchovies'
#	print("Hold the anchovies!")#If False, Python returns the print statement,True otherwise

#next_section= print(f'\nCheckin for inequalities: Next Section\n')#magic_number.py

#answer = 15

#if answer != 42:
#	print("That is not the correct answer. Please Try again!\n")
#The conditional test passes, since the answer is not = 17, the intended code block is executed

#requested_toppings = 'pepperoni'or'pinapple'#Here I'm checking if these items are in the fridge

#if requested_topping != ['mushrooms','onions','pinapple']: #These are the only registered items in my list
#	print(f'Google add {requested_toppings} to shopping list!')#make request to add to shopping list if missing or low
