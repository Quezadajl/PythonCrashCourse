#User Input as parrot.py
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)
#for these exercises, use your terminal to get the input prompt

#greeter.py sample
#name = input("Please enter your name: ")
#print(f"\nHello,{name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
prompt += "\nWhat is your last name? "

name = input(prompt)
print(f"\nHello, {name}!")