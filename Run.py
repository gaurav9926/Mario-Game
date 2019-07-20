from mario import *
from header import *
from Enemy import *
import os
import time
import termios
import signal
import errno
import threading
import sys
import random as r
from functools import wraps
TERMIOS = termios
timeout_value = 0.1


mario = Mario(0,32)



def check():
    if level == 1 or level == 2:  
        if arrr[mario.y+2][mario.x] == ' ' and arrr[mario.y+2][mario.x+1] == ' ':
            mario.deleteMario(arrr)
            mario.y += 1
        if mario.y > 38:
            header.lives -= 1
            print("ONE LIFE LOST!!")
            mario.x = t
            mario.y = 32    
        if header.lives == 0:
            header.end(level,-1)
            return 0
        else: 
        	return 1            	

def printBoard(board):
	arr2 = mario.printMario(arrr,mario.x,mario.y)
	tmp = ['' for i in range(0,42)]
	for x in range(0,42):
		for y in range(t,t+60):
			tmp[x] = tmp[x] + arr2[x][y]
	for x in range(0,42):
		print(tmp[x])




def timeout(seconds, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise Exception(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator
@timeout(0.1)
def getkey():
        start = time.time()
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
            c = os.read(fd, 1)
        finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c
up = -1
right = -1
t=0
var1 = 1
var2 = 1
arr = []
vartime=0
flag = 0
level = int(1)
if level == 1:
	enemy1 = Enemy1(98)
	enemy2 = Enemy1(128)
	arrr , board  = firstlevel()
else:
	arrr , board  = secondlevel()

def Jump(arrr):
	cnt = 0
	if arrr[mario.y][mario.x-1] == ' ':
		while arrr[mario.y-1][mario.x] == ' ' and up == 1 and arrr[mario.y-1][mario.x+1] == ' ':
			cnt += 1
			if cnt == 8:
				break
			arrr = mario.deleteMario(arrr)	
			mario.y -= 1
			arrr = mario.printMario(arrr,mario.x,mario.y)

if __name__ == "__main__":
	while True:
		flag = 0
		os.system('clear')
		header.printheader()
		printBoard(board)
		if level == 1:
			if var1 != -1:
				arrr = enemy1.printEnemy(arrr,enemy1.x)
			if var2 != -1:	
				arrr = enemy2.printEnemy(arrr,enemy2.x)
		if vartime == 10:
			vartime = 0
			header.timer()
			if level == 1:
				if var1 != -1:
					enemy1.moveEnemy(arrr)
				if var2 != -1:	
					enemy2.moveEnemy(arrr)
		if level == 1:
			if enemy1.x == 76:
				arrr = enemy1.deleteEnemy(arrr)
				enemy1.x = 98
				arrr = enemy1.printEnemy(arrr,enemy1.x)
			if enemy2.x == 105:
				enemy2.deleteEnemy(arrr)
				enemy2.x = 128		
				arrr = enemy2.printEnemy(arrr,enemy2.x)
			if mario.x == enemy1.x and mario.y == 31 and var1 != -1:
				var1 = -1
				arrr = enemy1.deleteEnemy(arrr)
				enemy1.x = 1000
				header.score += 100
			if mario.x + 2 == enemy1.x and mario.y == 32:
				mario.deleteMario(arrr)
				header.lives -= 1
				if arrr[32][t] == ' ':	
					mario.x = t	
				
			if mario.x == enemy2.x and mario.y == 31 and var2 != -1:
				var2 = -1
				arrr = enemy2.deleteEnemy(arrr)
				header.score += 100
				enemy2.x = 1000
			if mario.x + 2 == enemy2.x and mario.y == 32:
				mario.deleteMario(arrr)
				header.lives -= 1
				if arrr[33][t] == ' 'and arrr[33][t+1] == ' ':	
					mario.x = t	
			
		if arrr[mario.y+2][mario.x]=='C' :
			arrr = mario.deleteMario(arrr)
			arrr[mario.y+2][mario.x] == ' '
			header.score += 10
			mario.y += 2
		if arrr[mario.y+2][mario.x+1]=='C' :
			arrr = mario.deleteMario(arrr)
			arrr[mario.y+2][mario.x+1] == ' '
			header.score += 10
			mario.y += 2		
		right = -1
		up = -1
		try :
			k = getkey()
		except:
			k = None	
		if k == b'q':
			header.end(level,1)
			sys.exit()
		if k == b'd':
			right = 1
			if arrr[mario.y][mario.x+2] == ' ' and arrr[mario.y+1][mario.x+2]==' ':
				mario.deleteMario(arrr)
				mario.x += 1
			if check() == 0:
				break
			if arrr[mario.y][mario.x + 2]=='C' :
				header.score += 10
				arrr[mario.y][mario.x+2] = ' '
				mario.deleteMario(arrr)
				mario.x += 1
			if arrr[mario.y+1][mario.x+2]=='C':
				header.score += 10
				arrr[mario.y+1][mario.x+2] = ' '
				mario.deleteMario(arrr)
				mario.x += 1						
		elif k == b'a':
			if mario.x - t > 0 and arrr[mario.y][mario.x-1]==' ' and arrr[mario.y+1][mario.x-1]==' ' :
				mario.deleteMario(arrr)
				mario.x -= 1
			if arrr[mario.y][mario.x-1]=='C' :
				header.score += 10
				arrr[mario.y][mario.x-1] = ' '
				mario.deleteMario(arrr)
				mario.x -= 1
			if arrr[mario.y+1][mario.x-1]=='C':
				header.score += 10
				arrr[mario.y+1][mario.x-1] = ' '
				mario.deleteMario(arrr)
				mario.x -= 1			
			if check()	== 0:
				break		 
		elif k == b'w' and mario.y > 20:
			up = 1
			Jump(arrr)
			if arrr[mario.y-1][mario.x]=='C':
				header.score += 10
				arrr[mario.y-1][mario.x] = 'C' 		
				mario.deleteMario(arrr)
				mario.y -= 1
			if arrr[mario.y-1][mario.x+1]=='C':
				header.score += 10
				arrr[mario.y-1][mario.x+1] = 'C' 		
				mario.deleteMario(arrr)
				mario.y -= 1
		else:
			if check() == 0:
				break
		if mario.x - t > 42:
			t += 1
		if mario.x >= 143 :
			level += 1
			if level == 2:
				t=0
				header.score += header.time
				header.time = 60
				mario.x = 0
				mario.y = 32
				arrr , board  = secondlevel()
		if int(level) > 2:
			header.end(level,-1)		
		vartime = vartime + 1
	






