motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#appending to the end of a list
motorcycles.append('ducati')
print(motorcycles)
#changing, adding and removing elements in a list; makes it easier to build lists dynamically
motorcycles[0] = 'BMW'
print(motorcycles)#the code shows that we replaced the first element by re-defining a new list
#Inserting Elements into a List
my_doggies = []
my_doggies.append('Martin')
my_doggies.append('Sophie')
my_doggies.append('Alolamola')

print(my_doggies)
#Deleting and Inserting in an element in a specific place
del my_doggies[2]
print(my_doggies)