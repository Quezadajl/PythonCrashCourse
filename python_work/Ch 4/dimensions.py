#Tuples - python refers to values that cannot change as immutable, and an immutable list is called a tuple
#Tuples can still be indexed/sliced
dimensions = (200, 50) # Tuples use parantheses instead of square brackets
print(dimensions[0])
print(dimensions[1])
print(dimensions[:1])
#Lets try to change one of the items
dimensions[0] = 150
print(dimensions)#error code reads : 'tuple' object does not support item assignment