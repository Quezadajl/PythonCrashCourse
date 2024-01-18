#Slicing, outputting a specific elements in a list
players = ['charles', 'martina','michael','florence','eli']
print(players[0:3]) #Here we recall the first three elements
print(players[:3]) # omitting the first index, python starts from the first element
print(players[2:])# you can also start with the third element and index all the way through
print(players[-3:])#using a negative pulls the last elements of the list
#print(players[0:3:2])#A third number allows you to skip slice the list
#print(players)


#Using Looping through a slice
#names = ['martin', 'sophie', 'lola', 'ash', 'taylor','chikorita']
#print("Here are the first three players on my team:")
#for player in names[:3]:
#	print(player.title())
	#Instead of looping through the entire list, Python loops through only the first three names

#Practice: Slicing with Numbers
#number = [value for value in range(1,51)] #practicing for loops
#number.insert(-1,'hola')#Inserting into a list
#print(number[-5:])#Using the negative as an example of pulling the last 5 entries or most recent on dataset

#Practice: Slicing with Numbers
#digit = [number for number in range(1,10000000)]
#digit.insert(-1,'3.14')
#print(digit[-4:])

#Practice 4.10
#print(f'\nThe first three items in the list are:{names[:3]}')
#print(f'\nThe middle three items in the list are:{names[2:5]}')
#print(f'\nThe last three items in the list are:{names[-3:]}')

