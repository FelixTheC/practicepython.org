#! /usr/env/python3

def removeDoublesSet(liste):
    tempListe = set(liste)
    newListe = list(tempListe)
    return newListe

def removeDoubles(liste):
    tempListe = []
    for item in liste:
        if item not in tempListe:
            tempListe.append(item)    
    return tempListe

if __name__ == '__main__':
    liste = [1,1,2,3,4,5,5,6,7,7,8,8,9]
    print(removeDoubles(liste))
    print('#'*30)
    print(removeDoublesSet(liste))