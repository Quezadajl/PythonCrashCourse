for value in range(1,5):
	print(value)
	#the off-by-one behavior programming languages have
	#The range() function causes Python to start counting at the first value you give it, and stops when it reaches the 2nd value

for values in range(6):
	print(values)
	#with only one argument it returns the numbers in between 0 to 5
#Using range() to make a list of numbers
numbers = list(range(7))
print(numbers)