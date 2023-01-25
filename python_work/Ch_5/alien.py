alien_0 = {'color':'green','points': 5} # using braces with semicolons to store information; Dict
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)

alien_0['x_position'] = 0 #screen coordinates usually start at the upper-left corner of the screen
alien_0['y_position'] = 25 #Give the name of the dictionary followed by the new key in [ ] brackets
print(alien_0)