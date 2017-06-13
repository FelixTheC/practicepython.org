#! /usr/env/python3

def is_empty(liste=[]):
	"""
	Need a list as parameter and check if list len>0
	"""
	if len(liste) > 0:
		return False
	else:
		return True


def firstLast(liste):
	"""
	Need a list as paramater and returns 
	the first and the last element of these as new list
	"""
	listPiece = None
	if is_empty(liste) == False:
		listPiece = [liste[0], liste[-1]]
	print(listPiece)


if __name__ == '__main__':
	liste = [1,2,3,4,5,6,7,8,9]
	firstLast(liste)