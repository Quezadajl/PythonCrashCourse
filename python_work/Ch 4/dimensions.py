#Tuples - python refers to values that cannot change as immutable, and an immutable list is called a tuple
#Tuples can still be indexed/sliced
dimensions = (200, 50) # Tuples use parantheses instead of square brackets
print(dimensions[0])
print(dimensions[1])
print(dimensions[:1])
#Lets try to change one of the items
#dimensions[0] = 150 #error code reads : 'tuple' object does not support item assignment
my_t = (3,) #tuple with one element
print(my_t)

print(f'We can loop over all the values in a tuple using a for loop:\n')
dimensions = (100,50)
for dimension in dimensions:
	print(dimension)

#Writing over a tuple
dimensions = (200,50)
print("Original dimensions:\n")
for dimension in dimensions:
	print(dimension)
