my_foods = ['pizza','thai curry','tinga']
print(my_foods)
my_foods.insert(0,'briyani') #Insert added biriyani to where ever you appointed it to
my_foods[0] = ('tofu')
friend_foods = my_foods[:] #Using the colon with square brackets copies everything on the list for reusing a list
#We make a cop by asking for a slice w/o specifying any indices and store the copy list

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('Pho')
friend_foods.append('pupusas')
#These changes show that we have two different list that we can keep adding things to them individually 
print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)