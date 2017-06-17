#! /usr/env/python3

from random import randint


def numberToGuess():
    theNum = randint(1000, 9999)
    numbers = [int(num) for num in str(theNum)]
    return numbers


def userNumber():
    while True:
        user = input('Type in your 4 digit number: ')
        try:
            if len(user) == 4 and int(user) > 999:
                break
        except ValueError:
            print('I told you to type in a 4 digit number ')
    userNums = [int(num) for num in user]
    return userNums


def cowOrBull(guess, user):
    cowsBulls = [0,0]
    i = -1
    for num in user:
        i += 1
        if num in guess and num != guess[i]:
            cowsBulls[0] += 1
        elif num == guess[i]:
            cowsBulls[1] += 1
    return cowsBulls
        
        
def main():
    guess = numberToGuess()
    while True:
        user = userNumber()
        cowboy = cowOrBull(guess, user)
        print('%d cows, %d bulls' % (cowboy[0], cowboy[1]))
        if cowboy[1] == 4:
            break
    print('You won')




if __name__ == "__main__":
    main()
