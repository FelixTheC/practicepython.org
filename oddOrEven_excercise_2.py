#! /usr/env/python3

checknum = input('Please type in a number to check if it even or odd: ')
try:
    #check even or odd
    if int(checknum)%2 == 0:
        print('Your number is even')
    else:
        print('Your number is odd')
    #check if the number is a multiple of 4
    if int(checknum)%4 == 0:
        print('Your number is also a multiple of 4')
    else:
        print('Your number is not a multiple of 4')
except:
    print('Your input must be a number')
    
num = input('Please type in your first number: ')
check = input('Please type in your second number: ')
try:
    dividend = int(num)/int(check)
    if dividend%2 == 0:
        print('Your division is evenly')
    else:
        print('Your divivsion is not evenly')
except:
    print('Check if your input was realy a number')