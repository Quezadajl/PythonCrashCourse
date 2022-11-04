my_foods = ['pizza','thai curry','tinga']
print(my_foods)
my_foods.insert(-1,'briyani') #Insert added biriyani to where ever you appointed it to; in this case at the end
my_foods[0] = ('tofu') #replaced pizza with tofu
friend_foods = my_foods[:] #Using the colon with square brackets copies everything on the list for reusing a list
#We make a copy by asking for a slice w/o specifying any indices and store the copy list

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

#Practice 4-11
#4.1 Challenge redux
pizza = ['pepperoni', 'pinapple','cheese']
for flavors in pizza:
	print(f'I love {flavors} pizza!\n')
print(f'I can eat {pizza[0]} pizza all the time, but the {pizza[1]} pizza with jalapenos is my favorite!\n')

friends_pizza = pizza[:]
print(friends_pizza)
friends_pizza.append('jalapenos')
print(pizza)
print(friends_pizza)