#Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython") #applying a tab to my code with \t
print("\nPython") #applying a new line to my code with \n

print("Languages: \n\tPython\nC\nJavaScript") #applying a newline with \n
	#additionally combine them to \n & \t for new lines and tab the statement


#Stripping whitespace
favorite_language = 'python '
print(favorite_language.rstrip()) #right strip of whitespace
 #lstrip clears whitespace from the left of the space
 #strip clears whitespace on both sides of the comment/sentence

 #Practice: stripping whitespace
developer_language = ' .  Python    .  ' 
print(developer_language.rstrip())
print(developer_language.lstrip())
print(developer_language.strip())


#practice_clean
code = 'clean'
dirty = ' space'
print(code.rstrip())
print(dirty)
print(dirty.strip())