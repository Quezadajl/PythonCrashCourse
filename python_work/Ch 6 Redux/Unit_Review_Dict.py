#alien.py
alien_0= {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
#We start by defining the same dictionary that we've been working with
print(alien_0)

#Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#changing the key of a value pair
alien_0['color'] = 'yellow'
print(F"The alien is now {alien_0['color']}.")
print(alien_0)


#Tracking values
alien_0 = {'x_position':0, 'y_position':25,'speed':'fast'} #replace speed with other keywords stablished under the if-elif-else statement
print(f"Original position: {alien_0['x_position']}")
#Move the alien to the right
#Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

#the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New Position: {alien_0['x_position']}")

#Removing Key-value Pairs
#alien.py
alien_0= {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
#We start by defining the same dictionary that we've been working with
print(alien_0)
del alien_0['points'] #points has been removed
print(alien_0)