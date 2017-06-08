#! /usr/env/python3

"""
A nice little game how the names say's it's the game rock scissor paper
You can choose player vs player or player vs computer
"""

from random import choice
import getpass


def checkInput(player):
	figures = ['rock', 'scissor', 'paper']
	fig = ''
	while True:
		fig = getpass.getpass(player + ' your are ')
		if fig in figures:
			fig = fig
			break
	return fig


def checkWin(player1_choice, player2_choice):
	figureDic = {'scissor': 'paper', 'paper': 'rock', 'rock': 'scissor'}
	win = ''
	if figureDic[player1_choice] == player2_choice:
		win = 'player1'
	elif figureDic[player2_choice] == player1_choice:
		win = 'player2'
	else:
		win = 'draw'
	return win


def game():
	pvc = input('Do you play alone? y/n ')
	listOfWins = [0,0]
	rounds = 0

	if pvc == 'n':
		player1 = input('Hello player1 whats your name? ')
		player2 = input('Hello player2 whats your name? ')

		while True:
			player1_choice = checkInput(player1)
			player2_choice = checkInput(player2)

			if checkWin(player1_choice, player2_choice) == 'player1':
				print(player1 + ' wins!!! ' + player1_choice + ' ' + player2_choice)
				listOfWins[0] = listOfWins[0]+1
			elif checkWin(player1_choice, player2_choice) == 'player2':
				print(player2 + ' wins!!!! ' + player1_choice + ' ' + player2_choice)
				listOfWins[1] = listOfWins[1]+1
			else:
				print('Draw')

			rounds += 1

			quit = input('Quitting the game?? y/n ')
			if quit == 'y':
				break

	else:
		player = 'Player'
		figures = ['rock', 'paper', 'scissor']
		while True:
			player_choice = checkInput(player)
			comp_choice = choice(figures)
			
			if checkWin(player_choice, comp_choice) == 'player1':
				print('Player wins ' + player_choice + ' ' + comp_choice)
				listOfWins[0] += 1
			elif checkWin(player_choice, comp_choice) == 'player2':
				print('Computer wins ' + player_choice + ' ' + comp_choice)
				listOfWins[1] += 1
			else:
				print('Draw')
			
			rounds += 1
		
			quit = input('Quittin the game? y/n ')
			if quit == 'y':
				break
	

	print('After %s games the final result is %s ' %(rounds, listOfWins))
		



if __name__ == "__main__":
	game()		