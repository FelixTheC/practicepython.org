#! /usr/env/python3


def pipe():
    print(' ---' * 4)
          
          
def stack():
    print('|   ' * 5)

    
def board():
    for i in range(4):
        pipe()
        stack()
    pipe()
            
            
if __name__ == '__main__':
    board()