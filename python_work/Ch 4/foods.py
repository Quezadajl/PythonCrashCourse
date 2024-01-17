my_foods = ['pizza','thai curry','tinga']
print(my_foods)
my_foods.insert(-1,'briyani') #Insert added biriyani to where ever you appointed it to; in this case at the end
my_foods[0] = ('tofu') #replaced pizza with tofu
friend_foods = my_foods[:] #Using the colon with square brackets copies everything on the list for reusing a list
#We make a copy by asking for a slice w/o specifying any indices and store the copy list

print("My favorite food are:")
print(my_foods)
friend_foods.insert(-1,'Potato Salad')
friend_foods[0] =('albondigas')
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('Pho')
friend_foods.append('pupusas')
#These changes show that we have two different list that we can keep adding things to them individually 
print("\nMy UPDATE list of favorite food are:")
print(my_foods)

print("\nMy friend's UPDATE list of favorite foods are:")
print(friend_foods)

#Practice 4-11
#4.1 Challenge redux
pizza = ['pepperoni', 'pinapple','cheese']
for toppings in pizza:
	print(f'\nI love {toppings} pizza!\n')
print(f'I can eat {pizza[0]} pizza all the time, but the {pizza[1]} pizza with jalapenos is my favorite!\n')

friends_pizza = pizza[:] #creating a copy of the pizza list
print(friends_pizza)
pizza.append('jalapenos')
friends_pizza.insert(3,'ham')
#print(pizza)
#print(friends_pizza)
print(f"\nMy friend's favorite pizzas are:")
for toppings in pizza:
	print(f"{toppings} pizza!\n")

#Challenge 4-12 More Loops
print(f" My favorite foods are:")
for dishes in my_foods:
	print(f"{dishes.title()}!\n")

print(f"Some of Tania's favorite foods include:")
for treats in friend_foods:
	print(f"{treats.title()}!\n\t")