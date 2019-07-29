class Board:
	def __init__(self,col):
		self.col = col

	def gamearea(self):	
		board = [[] for i in range (0,42)]
		normalrow = []
		groundrow = []
		for i in range(0, self.col):
			groundrow.append('X')
		for i in range(0, self.col):
			normalrow.append(' ')
		for i in range(0, 42):
			if i < 2 or i >= 34:
				board[i] = groundrow[:]
			else:
				board[i] = normalrow[:]
		return board		

	def create(self,arr,hor,ver,s):
		for i in range(0,2):
			for j in range(0,2):
				arr[ver+i][hor+j] = s
		return arr
	
	def bricks(self,arr,hor,ver,len):
		for i in range(0,len,2):
			tmp = self.create(arr,hor+i,ver,'=')
		return tmp

	def tunnels(self,arr,hor,h):
		for i in range(0,h):
			for j in range(0,h):
				tmp = self.create(arr,hor+i,32-j,'T')
		for i in range(0,h):	
			tmp = self.create(arr,hor+i,32-h,'+')
		tmp = self.create(arr,hor,32,'T')
		return tmp

	def cloud(self,board,hor,ver):
		board[ver][hor+1] = 'c'
		board[ver+1][hor+1] = 'c'
		board[ver+2][hor+1] = 'c'
		board[ver][hor+2] = 'c'
		board[ver+2][hor+2] = 'c'
		board[ver+1][hor+2] = 'c'
		board[ver+1][hor] = 'c'
		board[ver+1][hor+3] = 'c'
		return board
	def end(self,arr,x):
		arr[32][x] = '|'		
		arr[32][x+1] = '|'		
		arr[33][x+1] = '|'		
		arr[33][x] = '|'
		arr[32][x] = "("
		arr[32][x+1] = ")"
		return arr	

class Board2():
	def __init__(self,col):
		self.col = col
	def gamearea(self):	
		board = [[] for i in range (0,42)]
		normalrow = []
		groundrow = []
		for i in range(0, self.col):
			groundrow.append('X')
		for i in range(0, self.col):
			normalrow.append(' ')
		for i in range(0, 42):
			if i < 28 or i >= 34:
				board[i] = groundrow[:]
			else:
				board[i] = normalrow[:]
		return board
	def makegap(self,arr,x,y):
		for i in range(x,y):
			for j in range(0,9):
				arr[33+j][i] = ' '	
		return arr				
	def create(self,arr,x,y,len,s):
		for i in range(0,len):
			arr[y][x+i] = s
		return arr	
	def end(self,arr,x):
		arr[32][x] = '|'		
		arr[32][x+1] = '|'		
		arr[33][x+1] = '|'		
		arr[33][x] = '|'
		arr[32][x] = "("
		arr[32][x+1] = ")"
		return arr			


