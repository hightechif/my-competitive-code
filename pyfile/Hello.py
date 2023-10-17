# Hello.py : This program say hello and ask for your name.
# Ridhan Fadhilah, 12-01-2016
print('Hello World!')
print('What is your name?')   # ask for their name
myName = input()
print('it is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
