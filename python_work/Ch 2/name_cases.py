 #Personal Message
first_born = "  Sophie "
second_born = "    Martin"
third_born = "Lola  "
my_babies = f"   Hello love of my life {first_born.strip()}, {second_born.strip()}, and {third_born.strip()}!"
print(first_born.strip())
print(second_born.lstrip())
print(third_born.strip())
print(my_babies.strip())

#Name cases
first_name = "Jose" # variable
last_name = "Quezada" #variable
full_name = f"{first_name} {last_name}" # created a function to combine the variables

print(full_name.upper()) #all capitalized
print(full_name.lower()) #all lowercased
print(full_name.title()) #First letter of each word capitalized
print(my_babies.title().strip()) #testing multiple methods in the with strings

#FamousQuote
author = "Thor  "
quote = "  ... still worthy!  "
motivation = f"{quote}! -{author}"
print(motivation.strip())

#stripping names
print("pokemon:Cyndaquil\n\tType:\n\t\tFire") 