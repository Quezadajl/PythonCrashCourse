bicycles = ['trek','cannondale','redline', 'specialized']
#print(bicycles)
print(bicycles[0])
#accessing any element in a list by telling python the position, or INDEX starting at 0
#mix index with formating
print(bicycles[0].title())
print(bicycles[-1].upper())# index -1 always returns the last item on the list
####
message=f"\nMy first bicycle was a {bicycles[2].title()}."#using f-strings in messages w/indexes
print(message)
###Excersis 3-1##
names = ['martin','sophie','lola','Tania']
print(names[0])
##greetings##
greetings = f"\n{names[2]} really likes to follow {names[0]} when he chases the {bicycles[-4]} while {names[1]} just watches"
print(greetings.title())

#Practice
all_is_good = f"\n{names[0]} on the couch, {names[1]} on her beanbag, and {names[-2]} sorrounded by shoes\n\t...all is good...\n\t at home"
print(all_is_good)