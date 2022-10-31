my_foods = ['pizza','thai curry','tinga']
my_foods.append('Pho')
my_foods.insert(-1,'biryany')
friend_foods = my_foods[:] #Using the colon with square brackets copies everything on the list for reusing



print("My favorite food are:")
print(my_foods)

print("\nMy frined's favorite foods are")
print(friend_foods)