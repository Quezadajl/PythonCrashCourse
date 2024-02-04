#Nesting: a lits of items inside a dictionary
alien_0 = {'color':'green', 'point':5}
alien_1 = {'color':'yellow', 'point':10}
alien_2 = {'color':'red', 'point':15}

aliens = [alien_0,alien_1,alien_2] # here is where the nesting takes place; a list of dictionaries

#loop through it
for alien in aliens:
 print(alien)