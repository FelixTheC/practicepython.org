#! /usr/env/python3

from random import randint

list_1 = []
list_2 = []
commonList = []
for i in range(10):
    list_1.append(randint(1,99))
for j in range(12):
    list_2.append(randint(1,99))

if len(list_1) > len(list_2):
    for item in list_1:
        if item in list_2 and (item not in commonList):
            commonList.append(item)
else:
    for item in list_2:
        if item in list_1 and (item not in commonList):
            commonList.append(item)
            
print(list_1)
print(list_2)
print(commonList)