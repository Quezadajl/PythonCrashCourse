#Practicing if && if-else statements
age = 71
#age = 17
if age >= 18:
	print('You are old enough to vote!')
	print('Have you registered to vote yet?')
else:
	print('Sorry you are too young to vote')
	print('Pleae register to vote when you turn 18!')#All indented lines after an if statement will execute

#Simple conditional tests: if conditional test: do something

#AMUSEMENTPARK.PY
#The if-elif-else Chain
if age <= 4:
	print('admission is free')
elif age <18:
	print('admission is $25')
else:
	print('18 and older pay $40')

#Improved VERSION
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f'Your admission cost is ${price}.')# improved maintaince by only have to modify one message

