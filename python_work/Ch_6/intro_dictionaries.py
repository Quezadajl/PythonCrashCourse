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

alien_0['speed'] = {'medium'}
print(alien_0)