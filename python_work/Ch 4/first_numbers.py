for value in range(1,5):
	print(value)
	#the off-by-one behavior programming languages have
	#The range() function causes Python to start counting at the first value you give it, and stops when it reaches the 2nd value

for values in range(6):
	print(values)
	#with only one argument it returns the numbers in between 0 to 5
#Using range() to make a list of numbers using the list() function
numbers = list(range(7))
print(numbers)

#creating list that skip-count
even_numbers = list(range(3,15,2))
print(even_numbers)

#creating lists that use exponents
squares = []
for value in range(11):
	squares.append(value**2)

print(squares)

#using simple statistics with a list of numbers
stats_list = list(range(1,20,2))
print(min(stats_list))
print(max(stats_list))
print(sum(stats_list))