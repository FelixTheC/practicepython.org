#! /usr/env/python3
from check_ticTacToe_excercise_26 import createList, checkWin

class TicTacToe():
    
    def __init__(self):
        self.game_board = self.board(4)
    
    
    def board(self,col):
        board = []
        for i in range(col):
            board.append(['_','_','_','_'])
        return board
    
    
    def showGameBoard(self,game_board):
        row = 3
        for item in game_board:
            print(str(row), item)
            row -= 1    
    
    
    def gamerAction(self):
        turn = input('Please make your turn (row, col): ')
        cordinates = turn.split()
        return cordinates
    
    
    def turnAllowed(self, board, cordinates):
        if board[3 - int(cordinates[0])][int(cordinates[1])] == 'x' or board[3 - int(cordinates[0])][int(cordinates[1])] == 'o':
            cordinates = [str(int(cordinates[0])+1),str(cordinates[1])]
            return cordinates
        elif cordinates[0] == '0':
            if board[3 - int(cordinates[0])][int(cordinates[1])] == 'x' or board[int(cordinates[0])][int(cordinates[1])] == 'o':
                cordinates = [str(int(cordinates[0])+1),str(cordinates[1])]
                return cordinates
            else:
                return cordinates
        else:
            return cordinates
    
    
    def computer(self):
        from random import choice
        possibleTurns = []
        for i in range(4):
            for j in range(4):
                possibleTurns.append([i,j])
        return choice(possibleTurns)
    
    
    def pvp(self):
        self.showGameBoard(self.game_board)    
        gamer_1 = self.turnAllowed(self.game_board, self.gamerAction())
        self.game_board[3 - int(gamer_1[0])][int(gamer_1[1])] = 'x'
        self.showGameBoard(self.game_board)
        gamer_2 = self.turnAllowed(self.game_board, self.gamerAction())
        self.game_board[3 - int(gamer_2[0])][int(gamer_2[1])] = 'o'        
    
    
    def pvc(self):
        self.showGameBoard(self.game_board)    
        gamer_1 = self.turnAllowed(self.game_board, self.gamerAction())
        self.game_board[3 - int(gamer_1[0])][int(gamer_1[1])] = 'x'
        gamer_2 = self.turnAllowed(self.game_board, self.computer())
        self.game_board[3 - int(gamer_2[0])][int(gamer_2[1])] = 'o'           


    def checkWinner(self):
        string = ''
        player1 = (checkWin(createList(self.game_board)[0]))
        player2 = (checkWin(createList(self.game_board)[1]))
        if player1 == 4 :
            string = 'Congratulations Player1 you won'
        elif player2 == 4:
            string = 'Congratulations Player2 you won'
        elif player1 == 4 and player2 == 4:
            string = 'Draw'
        else:
            string = 'Draw'
        return string
    
    
    def again(self):
        again = input('Do you want to play again y/n? ')
        if again == 'n':
            return False
        elif again == 'y':
            self.game_board = self.board(4)
            self.main()
    
    
    def main(self):
        playVsPc = input('Do you want to play vs the computer? j/n ')
        if playVsPc == 'n':
            while True:
                self.pvp()
                if '_' not in self.game_board[0]:
                    break
            print(self.checkWinner())
            if self.again() == False:
                return False
        elif playVsPc == 'j':
            while True:
                self.pvc()
                if '_' not in self.game_board[0]:
                    break
            print(self.checkWinner())
            if self.again() == False:
                return False
        else:
            print('Please check your input')


if __name__ == '__main__':
    game = TicTacToe()
    game.main()