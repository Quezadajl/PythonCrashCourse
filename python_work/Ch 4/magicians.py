magicians = ['alice','david','carolina'] #Defining the list
for magician in magicians: #use the for loop as "for every magician in the list of magicians, print the magician's name"
	print(magician)
# We tell python to print the name that's just been assigned to the variable magician.

babies = ['Martini-whinnie','Sophilicious','Lomitalomation']
for doggies in babies: #doggies is the variable I assigned to each print of the list babies
	print(f'\n{doggies} is the best at cuddling\n')
	print(f'\n{doggies} you are the best!\n')
print("thank you for being so unique in personalities")

magicians = ['alice','david','carolina'] #Defining the list
for magician in magicians: #use the for loop as "for every magician in the list of magicians, print the magician's name"
	print(f'\n{magician.title()}, that was a great trick!\n')
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")# Using print without the indentation does not go with the loop

#4.1 Challenge
pizza = ['pepperoni', 'pinapple','cheese']
for toppings in pizza:
	print(f'I love {toppings} pizza!\n')
print(f'I can eat {pizza[0]} pizza all the time, but the {pizza[1]} pizza with jalapenos is my favorite!')

#4.2 Challenge
animals = ['dog', 'dragon', 'plant']
for pets in animals:
	print(f'I believe that a {pets} makes the best pets!\n\t')

#Practice
artists = ['Moderatto', 'The Killers', 'Taylor Swift','Olivia Rodrigo','Daniel Me Estas Matando!']
for artist in artists:
	print(f'I can listen to {artist} all day!\n\t')

