#Practicing if && if-else statements
age = 19
#age = 17
if age >= 18:
	print('You are old enough to vote!')
	print('Have you registered to vote yet?')
else:
	print('Sorry you are too young to vote')
	print('Pleae register to vote when you turn 18!')#All indented lines after an if statement will execute

#Simple conditional tests: if conditional test: do something

#The if-elif-else Chain
if age <= 4:
	print('admission is free')
elif age >4 and age <18:
	print('admission is $25')
else:
	print('18 and older pay $40')