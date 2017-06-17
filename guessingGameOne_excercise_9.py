#! /usr/env/python3
from random import randint

theNum = randint(1, 9)
guess = 0

while True:
	user = input("Your guess or 'exit' to quit ")
	if user == 'exit':
		break
	else:	
		try:
			if int(user) == theNum:
				guess += 1
				print('You did it, you guess the right number after %s guesses' % (guess))
				break
			elif int(user) < theNum:
				guess += 1
				print('Your guess was to low')
			elif int(user) > theNum:
				guess += 1
				print('Your guess was to high')
		except:
			print('Please check your input')

