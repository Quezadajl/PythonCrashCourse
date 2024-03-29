squares = [] #Start with an empty list called squares
for value in range(1,11): #We tell Python to loop through each value from 1 to 10 using the range() function
	square = value**2 #Inside the loop, the current value is raised to the 2nd power
	squares.append(square) #each new value will be raised to the 2nd square

print(squares)

#Now for the clean-high level version of the above
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#another way to calculate a loop each value from 1 through 10
square_2 = [value**2 for value in range(1,11)] #here we are using exponents to the 2nd power
print(square_2)