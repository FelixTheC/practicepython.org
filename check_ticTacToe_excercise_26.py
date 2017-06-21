#! /usr/env/python3

def createList(liste):
    one = []
    two = []    
    for h in range(0,4):
        for i in range(0,4):
            winner = liste[h][i]
            if winner == 'x':
                one.append([h,i])
            elif winner == 'o':
                two.append([h,i])            
    return [one,two]


def checkWin(liste):
    numOne = liste[0][1]
    counter = 0
    if numOne != 0 and numOne != 3:
        for item in liste:
            if item[1] == numOne:
                counter += 1
    elif numOne == 0:
        for item in liste:
            if item[1] == numOne:
                counter += 1
        if counter < 4:
            counter = 0
            for item in liste:
                if item[1] == numOne:
                    counter += 1
                    numOne += 1
    elif numOne == 3:
        for item in liste:
            if item[1] == numOne:
                counter += 1
        if counter < 4:
            counter = 0
            for item in liste:
                if item[1] == numOne:
                    counter += 1
                    numOne -= 1
    return counter
