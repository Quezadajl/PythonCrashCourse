alien_0 = {'color':'green','points': 5} # using braces with semicolons to store information; Dict
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)

alien_0['x_position'] = 0 #screen coordinates usually start at the upper-left corner of the screen
alien_0['y_position'] = 25 #Give the name of the dictionary followed by the new key in [ ] brackets
print(alien_0)

#starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print(f"The alien is now {alien_0['color']}.")

alien_0['color'] = 'yellow' #modifying values in a dictionary
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original position: {alien_0['x_position']}")
#alien_0['speed'] = 'fast'
#Move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien.
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

alien_0 = {'color':'green','points': 10}
print(alien_0)

del alien_0['points']
print(alien_0)