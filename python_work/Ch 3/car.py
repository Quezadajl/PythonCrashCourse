cars = ['bmw', 'audi', 'toyota', 'subaru'] #upper or lower case can impact how the list is sorted permenantly
cars.sort()
print(cars)
#Python's sort() method makes it relatively easy to sort a list
cars.sort(reverse=True) #the reverse argument reverses ABD order
print(cars)
print('\nHere is the original list:')
print(cars)
print('\nHere is the sorted list:')#The sorted function is a temporary sorting option
print(sorted(cars))
#print("\nHere is the original list again")
#print(cars)

#Reverse chronological order
cars.reverse()
print(cars)

#finding the length of a list
#length = len(cars)
#print(length)