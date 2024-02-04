#Nesting: a lits of items inside a dictionary
alien_0 = {'color':'green', 'point':5}
alien_1 = {'color':'yellow', 'point':10}
alien_2 = {'color':'red', 'point':15}

aliens = [alien_0,alien_1,alien_2] # here is where the nesting takes place; a list of dictionaries

#loop through it
for alien in aliens:
 print(alien)

#In reality, lets automate this using range()
#Make an empty list for storing aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color':'green', 'point':5}
	aliens.append(new_alien)

#Show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")