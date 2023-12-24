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

print(f"The last motorecycle I owned was a {last_owned.title()}.")
#Pop() can be used to pull items from any part of the list

young_pup = my_doggies.pop()
print(young_pup)
print(f'The youngest puppy we have is {young_pup.title().strip()}.')


