#! /usr/env/python3
from datetime import datetime

year = datetime.now().year
userInfo = input('Hi whats your (pre)name and how old are you? ')
userInfoList = userInfo.split()
name = userInfoList[0]
try:
    age = userInfoList[1]
    bornYear = int(year)-int(age)
    yearHundret = bornYear + 100
    anwser = str(name)+' will get 100 years old in '+ str(yearHundret)
    print(anwser)
    often = input('type in a number ')
    print(int(often)*(anwser + '\n'))
except:
    print('Please type in your age after your (pre)name')