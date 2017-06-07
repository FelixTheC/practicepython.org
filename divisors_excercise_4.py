#! /usr/env/python3

num = input('Please put in a number ')
try:
    listOfAllDivivsors = []
    for i in range(1, int(num)):
        if int(num)%i == 0:
            listOfAllDivivsors.append(i)
    print('Here are all divisors of your number ', listOfAllDivivsors)
except:
    print('Please put in a number')