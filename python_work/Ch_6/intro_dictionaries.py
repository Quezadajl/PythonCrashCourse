x = ('Hello Dictionaries')
print(x)

alien_0 = {'color':'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#using dictionaries to store key-value pairs

new_points = alien_0['points']
print(f"You just earned {new_points} points")
#Redefined the dictionary & assigned it to a new variable

#Adding new key-value pairs to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#modifying a current Dictionary
alien_0['color'] = 'yellow'
print(alien_0)

#Tracking information based on if-elif-else statement

alien_0['speed'] = 'fast'
print(f"Original Position: {alien_0['x_position']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
#this must be a fast alien
	x_increment = 3

# The new position is the old position plus the increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing key-value pairs
alien_0 = {'color':'green', 'points': 5}

del alien_0['points']
print(alien_0)
#deleted key-value pairs are removed permanently


