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


for vehicle in auto:
	if vehicle == 'audi':
		print(True)
	else:
		print(False)

next_chapter = print(f'\nCheckin for inequalities: Next Section\n')