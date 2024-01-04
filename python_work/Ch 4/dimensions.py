#Tuples - python refers to values that cannot change as immutable, and an immutable list is called a tuple
#Tuples can still be indexed/sliced
dimensions = (200, 50) # Tuples use parantheses instead of square brackets
#print(dimensions[0])
#print(dimensions[1])
#print(dimensions[:1]) #using : counts everything from before or after if left blank
#Lets try to change one of the items
#dimensions[0] = (150) #Can't change it; error code reads : 'tuple' object does not support item assignment
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

#dimensions = (400,100)
#print('\nModified dimensions:')
#for dimension in dimensions:
#	print(dimension)

#Challenge 4-13
#buffet = ('rice', 'beans', 'guac', 'salsa', 'crema')#Create a tuple of 5 foods at a buffet
#print(buffet)
#for meal in buffet: #Create a for loop to print each item
#	print(meal)
#buffet[3] = ('fajitas') #tried to modify a tuple; immutable

#competition_buffet = buffet[:] #copy of the tuple# A list of desserts I like.
#desserts = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
#favorite_dessert = 'apple crisp'

# Print the desserts out, but let everyone know my favorite dessert.
#for dessert in desserts:
#    if dessert == favorite_dessert:
        # This dessert is my favorite, let's let everyone know!
#        print("%s is my favorite dessert!" % dessert.title())
#    else:
        # I like these desserts, but they are not my favorite.
#        print("I like %s." % dessert)
#print(competition_buffet)