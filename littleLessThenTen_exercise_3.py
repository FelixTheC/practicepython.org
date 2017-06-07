#! /usr/env/python3

list = [1,2,3,4,5,34,56,78,34,51,9,80]
print('given is a list ', list)
num = input('Please type in a number to search all less items from: ')
try:
    newList = [i for i in list if i < int(num)]
    print(newList)
except:
    print('Your input must be a number')