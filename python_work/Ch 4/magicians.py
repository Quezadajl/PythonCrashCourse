magicians = ['alice','david','carolina'] #Defining the list
for magician in magicians: #use the for loop as "for every magician in the list of magicians, print the magician's name"
	print(magician)
# We tell python to print the name that's just been assigned to the variable magician.

babies = ['Martini-whinnie','Sophilicious','Alolamola']
for doggies in babies:#doggies is the variable I assigned to each print of the list babies
	print(doggies)

magicians = ['alice','david','carolina'] #Defining the list
for magician in magicians: #use the for loop as "for every magician in the list of magicians, print the magician's name"
	print(f'{magician.title()}, that was a great trick!')
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")# Using print without the indentation does not go with the loop

#4.1 Challenge
pizza = ['pepperoni', 'pinapple','cheese']
for flavors in pizza:
	print(flavors)