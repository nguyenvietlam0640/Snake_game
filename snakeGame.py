

from tkinter import *
import tkinter
import random
from threading import Event
from tkinter.ttk import * 

winWidth = 1200
winHeight = 900
canvasWidth = winWidth-200
canvasHeight = winHeight-100
block = 50
speed = 100
score = 0
size =1	
mode = "freedom"
listTail = []
foodX = random.randrange(0,canvasWidth,block)
foodY = random.randrange(0,canvasHeight,block)
snakeX = random.randrange(0,canvasWidth,block)
snakeY = random.randrange(0,canvasHeight,block)

class Snake():
	def __init__(self,canvas,snakeX,snakeY):
		#initial
		self.canvas = canvas
		self.snakeX = snakeX
		self.snakeY = snakeY
		self.x = 0 
		self.y = 0
		self.snake = self.canvas.create_rectangle(self.snakeX,self.snakeY,
							self.snakeX+block,self.snakeY+block,fill="pink")
		self.lenght = 1
	
	def moveUp(self):
		self.x = 0
		self.y = -block
	
	def moveDown(self):
		self.x = 0
		self.y = block
	
	def moveLeft(self):
		self.y = 0
		self.x = -block
	
	def moveRight(self):
		self.y = 0
		self.x = block	

class Food():
	def __init__(self,canvas,foodX,foodY):
		#initial
		self.canvas = canvas
		self.foodX = foodX
		self.foodY = foodY
		self.food = self.canvas.create_rectangle(self.foodX,self.foodY,
							self.foodX+block,self.foodY+block,fill="purple")

def error():
	label.config(text = "this funtion does not exist ",fg = "red")

def gameOverString():
	global size
	label2 = tkinter.Label(canvas,text = "GAME OVER",fg = "red",bg = "grey",font=("Terminal",size))
	label2.place(x = canvasWidth//2-60-size*3-20, y = canvasHeight//2-50)
	size+=1
	label2.config(font=("Terminal",size))
	
	if size==50:
		size-=35
		newGameString()
	else:
		canvas.after(3,gameOverString)

def newGame():
	pass

def newGameString():
	showString = "---------------Press 'C' to leave---------------"
	label3 = tkinter.Label(canvas,text = showString,
							bg = "grey",font=("Terminal",size))
	label3.config(text = showString)
	label3.place(x =250, y = 600)
	def delay():
		label3.config(text = " ")
		canvas.after(500,newGameString)
	canvas.after(700,delay)
	
def meet():
		if snakeX == foodX and snakeY == foodY:
			return True
		else:
			return False

def gameLoop():

	global foodX
	global foodY
	global score
	global snakeX
	global snakeY
	snakeX+=snake.x 
	snakeY+=snake.y
	snakeHead = []
	snakeHead.append(snakeX)
	snakeHead.append(snakeY)
	listTail.append(snakeHead)

	def gameOver():
		global foodX
		global foodY
		global score
		global snakeX
		global snakeY
		status = False
		if mode =="box":
			if (snakeX<0 or snakeX>canvasWidth or 
				snakeY<0 or snakeY>canvasHeight):
					status = True
			else:
				for x in listTail[:-1]:
					if x == snakeHead:
						status = True

		elif mode =="freedom":
			if (snakeX<=0 or snakeX>=canvasWidth or 
				snakeY<=0 or snakeY>=canvasHeight):
					if snakeX<0:
						snakeX = canvasWidth
					elif snakeX>canvasWidth:
						snakeX = -block
					elif snakeY <0:
						snakeY = canvasHeight
					elif snakeY>canvasHeight:
						snakeY = -block
					else:
						pass

			else:
				for x in listTail[:-1]:
					if x == snakeHead:
						status = True
			return status

		else:
			pass

		return status


	if len(listTail)>snake.lenght:
		del listTail[0]

	snake.canvas.delete("all")
	food = Food(canvas,foodX,foodY)

	for x in listTail:
		snake.snake = snake.canvas.create_rectangle(x[0],x[1],
						x[0]+block,x[1]+block,fill="pink")

	if meet() == True:
		score+=1
		label.config(text = "score: "+str(score))

		
		snake.lenght+=1
		foodX = random.randrange(0,canvasWidth,block)
		foodY = random.randrange(0,canvasHeight,block)
		canvas.after(speed,gameLoop)

	elif gameOver():
		canvas.delete("all")
		gameOverString()
	
	else:
		canvas.after(speed,gameLoop)		
#main

win = Tk()
win.title("https://github.com/nguyenvietlam0640")
win.geometry(str(winWidth)+"x"+str(winHeight))
win.resizable(False,False)

label = tkinter.Label(win, text = "Score: " + str(score),font = ("Arial",30))
label.pack()
canvas = Canvas(win,width =canvasWidth,height = canvasHeight,bg = "grey")
canvas.pack()

snake = Snake(canvas,snakeX,snakeY)
food = Food(canvas,foodX,foodY)
gameLoop()

win.bind("<KeyPress-Up>",lambda e :snake.moveUp())
win.bind("<KeyPress-Down>",lambda e :snake.moveDown())
win.bind("<KeyPress-Left>",lambda e :snake.moveLeft())
win.bind("<KeyPress-Right>",lambda e :snake.moveRight())
win.bind("<KeyPress-c>",lambda e :win.destroy())
#win.bind("<KeyPress-n>",lambda e : error())
win.mainloop()