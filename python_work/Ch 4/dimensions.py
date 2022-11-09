#Tuples - python refers to values that cannot change as immutable, and an immutable list is called a tuple
#Tuples can still be indexed/sliced
dimensions = (200, 50) # Tuples use parantheses instead of square brackets
print(dimensions[0])
print(dimensions[1])
print(dimensions[:1])
#Lets try to change one of the items
#dimensions[0] = 150 #error code reads : 'tuple' object does not support item assignment
my_t = (3,) #tuple with one element
print(f'{my_t}\n')

dimensions = (200,50)
for dimension in dimensions:
	print(f'\n{dimension}')

#Writing over a tuple
dimensions = (200,50)
print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
	print(dimension)

#Challenge 4-13
buffet = ('rice', 'beans', 'guac', 'salsa', 'crema')
print(buffet)
for meal in buffet:
	print(meal)