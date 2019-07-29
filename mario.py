from board import *
from Enemy import *

class Mario():
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def printMario(self,arrr,x,y):
		for i in range(0,2):
			for j in range(0,2):
				arrr[y+i][x+j] = 'M'
		return arrr

	def deleteMario(self,arrr):
		for i in range(0,2):
			for j in range(0,2):
				arrr[self.y+i][self.x+j] = ' '
		return arrr		
			 
def firstlevel():
	board = Board(160)
	arrr = board.gamearea()
	arrr = board.create(arrr,20,30,'?')
	arrr = board.tunnels(arrr,70,5)
	arrr = board.bricks(arrr,28,25,6)
	arrr = board.tunnels(arrr,100,4)
	arrr = board.tunnels(arrr,130,4)
	arrr = board.end(arrr,144)
	for i in range(0,160,20):
		if i % 40 == 0:
			arrr = board.cloud(arrr,i,10)	
		else:
			arrr = board.cloud(arrr,i,6)	
	return arrr,board

def secondlevel():
	board = Board2(160)
	arrr = board.gamearea()
	arrr = board.create(arrr,4,32,32,'C')
	arrr = board.create(arrr,40,31,32,'=')
	arrr = board.create(arrr,43,29,32,'C')
	arrr = board.makegap(arrr,85,90)
	# arrr = board.create(arrr,85,31,4,'=')
	arrr = board.create(arrr,100,31,10,'C')
	arrr = board.create(arrr,98,32,32,'=')
	arrr = board.create(arrr,100,31,32,'C')
	arrr = board.end(arrr,143)
	return arrr,board			 


