#4.3
count = [value for value in range(1,21)]
#print(count)

#4.4 & 4.5
milli = [value for value in list(range(1,1000001))]
#print(milli)
#print(min(milli))
#print(max(milli))
#print(sum(milli))

#4.6
odd = [value for value in range(1,21,2)]
print(odd)

for value in range(1,21,2):
	print(value)

#4.7 & 4.8
threes = [value for value in range(3,33,3)]
print(threes)

#4.9 & 4.10
cubes = [value**3 for value in range(1,11)]
print(cubes)

cubes_2 = []
for cube in range(1,11):
	cubes_2.append(cube**3)
print(cubes_2)

