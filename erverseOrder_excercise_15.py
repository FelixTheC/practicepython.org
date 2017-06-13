#! /usr/env/python3

def getUserInput():
    text = input('Type in a short text ')
    return text

def reverseOrder(string):
    charList = string.split()
    reverse = ''
    for c in range(1, len(charList)+1):
        reverse += charList[-c]
        reverse += ' '
    return reverse


if __name__ == '__main__':
    print(reverseOrder(getUserInput()))