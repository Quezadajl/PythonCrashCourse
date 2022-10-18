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
last_owned = motorcycles.pop()
print(motorcycles)
print(last_owned)# pop() shows that ducati was removed from the end of the list and is now assigned to the variable last_owned

print(f"The last motorecycle I owned was a {last_owned.title()}.")
#Pop() can be used to pull items from any part of the list
treats = []
treats.append('pretzels')
treats.append('chocolate')
treats.append('coffee')
print(treats)

first_treat = treats.pop(1) #pop allows us to use an item that has been removed from the list
print(f'the first treat I really enjoyed was {first_treat.title()}.')

#Removing an item by value
motorcycles = ['honda', 'yamaha','suzuki', 'ducati']
print(motorcycles)

#Sometimes you won't know the position of the value you want to remove from a list. If you only know the value of the item you want..
#...to remove, you can use the remove() method
too_expensive = 'ducati'
motorcycles.remove(too_expensive) #we assiged the value to a variable; we then use this variable to tell python which value to remove
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

#Try it yourself challenge for Chapter 3
guest = []
guest.append('martinini')
guest.append('alola')
guest.append('Sophilicious')
print(guest)
print(f'The following person is invited to my dinner party: {guest[2]}')
print(f'The following person is invited to my dinner party: {guest[0]}')
print(f'The following person is invited to my dinner party: {guest[-2]}')