from mario import *
class Enemy1():
	def __init__(self,x):
		self.x = x
	def printEnemy(self,arr,x):
		arr[33][x] = 'E'
		arr[33][x+1] = 'E'
		return arr
	def deleteEnemy(self,arr):
		arr[33][self.x] = ' '
		arr[33][self.x+1] = ' '
		return arr
	def moveEnemy(self,arr):
		if arr[33][self.x-1] == ' ':
			self.deleteEnemy(arr)
			self.x -= 1
			self.printEnemy(arr,self.x)
		else:
			self.deleteEnemy(arr)
		return arr		


