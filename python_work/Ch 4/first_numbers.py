for value in range(1,5):
	print(value)
	#the off-by-one behavior programming languages have
	#The range() function causes Python to start counting at the first value you give it, 
	#  and stops when it reaches the 2nd value

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
#stats_list = []
#for value in list(range(2,10,2)):
#	stats_list.append(value**2)

#print(stats_list)
#print(min(stats_list))
#print(max(stats_list))
#print(sum(stats_list))

#List Comprehensions: Example below
#exponent = [ value**2 for value in range(11)]
#Descriptive name for the list and defining the expression with the values you want to store inside
#print(exponent)
#print(squares)
#This list compression composers the same function in one line instead of three or four
