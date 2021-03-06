#! /usr/env/python3

from random import choice

def get_word():
    """the word list is from http://norvig.com/ngrams/sowpods.txt
    """
    words = []
    try:
        with open('30_Pick_Word.txt', 'r') as f:
            for line in f:
                words.append(line.replace('\n','').lower())
    except FileNotFoundError:
        words = ['hamster','teddy']
    return choice(words)


def show_hidden_word(word):
    return ['_' for i in range(len(word))]
        
        
def open_hidden_field(hiddenliste, dic):
    for key in dic:
        hiddenliste[key] = dic[key]
    return hiddenliste


def char_in_word(char, word):
    """checks if a char is in the word therefore I created a dic because it could be that
    one char is more than one time in a word. 
    The key is the index and the right guest char is the value
    """
    dic = {}
    if char in word:
        for i in range(len(word)):
            if word[i] == char:
                dic[i] = char  
        return dic 
    else:
        return False
    
    
def create_word_from_list(wordListe):
    word = ''
    return word.join(wordListe)


def main():
    fails = 0
    print('Welcome to hangman')
    theWord = get_word()
    hidden = show_hidden_word(theWord)
    print(hidden)
    while True:
        user = input('Time for your guess ')
        check = char_in_word(user, theWord)
        if check:
            #everytime a guess is right the field turns into the char and will be shown
            print(open_hidden_field(hidden, check))
            if '_' not in open_hidden_field(hidden, check):
                print('You win '+ create_word_from_list(open_hidden_field(hidden, check)) + ' is the correct answer')
                break
        else:
            fails += 1
        if fails > 5:
            print('The correct answer is ' + theWord)
            break
    again = input('Do you want a new game y/n ')
    if again.lower() == 'y':
        main()
    else:
        print('Goodbye')
            
            
            
if __name__ == '__main__':
    main()
    