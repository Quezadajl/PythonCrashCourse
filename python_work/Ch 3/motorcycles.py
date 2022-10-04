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
#Deleting and Inserting in an element from a specific place as long as you know it's index
del my_doggies[2] #Use del and the index location to delete any element
print(my_doggies)

my_doggies.insert(2,'Lola') #Like del, you can use insert with the index number to add to a specific location
print(my_doggies)

#Using Pop() method removes the last item in a list, but it lets you work with that item after removing it.
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)# pop() shows that ducati was removed