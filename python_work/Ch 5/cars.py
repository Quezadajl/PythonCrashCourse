#Intro to if statements in python
cars = ['audi','bmw', 'subaru','toyota']

for car in cars:
	if car == 'bmw':#if the value of car is 'bmw'upper case
		print(car.upper())
	else:
		print(car.title())#if the value of car is anthing othar than 'bmw', title case it
