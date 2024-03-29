motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
#appending to the end of a list
motorcycles.append('ducati')
print(motorcycles)
#changing, adding and removing elements in a list; makes it easier to build lists dynamically
motorcycles[0] = 'BMW' #replacing
print(motorcycles)#the code shows that we replaced the first element by re-defining a new list
#Inserting Elements into a List

my_doggies = [] #started a new list and will be adding elements to it
my_doggies.append('Martin')
my_doggies.append('Sophie')
my_doggies.append('Alolamola')

print(my_doggies)
#Deleting and Inserting in an element from a specific place as long as you know it's index
del my_doggies[2] #Use del and the index location to delete any element
#Keep in mind that python starts from Zero
print(my_doggies)

my_doggies.insert(2,'Lola') #Like del, you can use insert with the index number to add to a specific location
print(my_doggies)

my_doggies.append('Lomitalomation!')
print(my_doggies)

############Practicing  Pop########

#Using Pop() method removes the last item in a list, but it lets you work with that item after removing it.
last_owned = motorcycles.pop()
print(motorcycles)
print(last_owned)# pop() shows that ducati was removed from the end of the list and is now assigned to the variable last_owned

print(f"\nThe last motorecycle I owned was a {last_owned.title()}.")
#Pop() can be used to pull items from any part of the list

young_pup = my_doggies.pop()
print(young_pup)
print(f'\nThe youngest puppy we have is {young_pup.title().strip()}.')


treats = []
treats.append('pretzels')
treats.append('chocolate')
treats.append('coffee')
print(treats)

first_treat = treats.pop(1) #pop allows us to use an item that has been removed from the list as long as you point to a position
print(f'\nthe first treat I really enjoyed was {first_treat.title()}.')

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

guest[0] = 'Martinwinnie'
guest[1] = 'Lomitalomation'
guest[2] = 'Sophie'
print(guest)

print(f'\n{guest[1]} can make it but someone else will replace them')
guest.append('Sandy') #adding a guest
guest[0] = 'Martin' #replacing martinwinnie
print(guest)

print(f'\nHello {guest} I will have a bigger table!')
guest.insert(0,'dantin')
guest.insert(2,'Myla')
print(guest)
len_guests = len(guest)
print(f'\nI will be inviting {len_guests} guests!')
print(f'\nThe following person is invited to my dinner party: {guest[0]}')
print(f'\nThe following person is invited to my dinner party: {guest[1]}')
print(f'\nThe following person is invited to my dinner party: {guest[2]}')
print(f'\nThe following person is invited to my dinner party: {guest[3]}')
print(f'\nThe following person is invited to my dinner party: {guest[4]}')

print(f'\nI am so sorry {guest}, I can only invite two of you!')
first_uninvited = guest.pop(2)
print(f'\nsorry {first_uninvited}, my table is smaller')
second_uninvited = guest.pop(0)
print(f'\nsorry {second_uninvited}, my table is smaller')
print(f'\nthanks {guest[0]} for bringing chips, thank you {guest[1]} for bringind dip, and thank you {guest[2]} for the drinks!')
print(guest)
del guest[0]
del guest[1]
del guest[0]
print(guest)