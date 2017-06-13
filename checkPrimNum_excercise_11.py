#! /usr/env/python3

def userInput(text='Please type in '):
	userInput = input(text)
	return userInput


def is_prime(number):
	"""
	Check if number is a prime number
	return True if it is and throws Exception if number is not a number
	"""
	try:
		for i in range(2, int(number)):
			if int(number)%i == 0:
				return False
			else:
				return True
	except Exception as e:
		return e


def main():
	number = is_prime(userInput('Please type in a number '))
	if number:
		print('Your number is a prime number')
	elif number == False:
		print('Your number is not a prime number')
	else:
		print(str(number))


if __name__ == '__main__':
	main()