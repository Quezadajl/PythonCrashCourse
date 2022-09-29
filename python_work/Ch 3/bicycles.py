bicycles = ['trek','cannondale','redline', 'specialized']
print(bicycles)
print(bicycles[0])
#accessing any element in a list by telling python the position, or INDEX starting at 0
#mix index with formating
print(bicycles[0].title())
print(bicycles[-1].upper())# index -1 always returns the last item on the list
####
message=f"My first bicycle was a {bicycles[2].title()}."#using f-strings in messages w/indexes
print(message)
###Excersis 3-1##
names = ['martin','sophie','lola','Tania']
print(names[0])
##greetings##
greetings = f"{names[2]} really likes to follow {names[0]} while {names[1]} just watches"
print(greetings)