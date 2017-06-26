#! /usr/env/python3

from random import choice

def getAWord():
    words = []
    with open('30_Pick_Word.txt', 'r') as f:
        for line in f:
            words.append(line.replace('\n','').lower())
    return choice(words)

def showHiddenWord(word):
    return ['_' for i in range(len(word))]
        

def openHiddenField(word, hiddenliste, dic):
    for key in dic:
        hiddenliste[key] = dic[key]
    return hiddenliste


def charInWord(char, word):
    dic = {}
    if char in word:
        for i in range(len(word)):
            if word[i] == char:
                dic[i] = char  
        return dic 
    else:
        return False
    
    
print(openHiddenField('narwal',showHiddenWord('narwal'),charInWord('a','narwal')))