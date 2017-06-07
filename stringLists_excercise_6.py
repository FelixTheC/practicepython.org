#! /usr/env/python3

string = input('Please type in a word: ')
stringBackwards = ''

for i in range(1,len(string)+1):
    stringBackwards += string[-i]

if stringBackwards == string:
    print('You typed in a palindrom')
else:
    print('You typed in a normal word')