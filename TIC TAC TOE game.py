import pygame, sys
import numpy as np

pygame.init()

Width = 600
Height = 600
Bg_Color = (0,0,0)
Sky = (0, 251, 255)
square_size = 200



screen = pygame.display.set_mode( (Width, Height) )
pygame.display.set_caption("TIC TAC TOE GAME")
screen.fill(Bg_Color)

Board = np.zeros( (3,3) )
#print(Board)


def draw_lines():
    pygame.draw.line(screen,Sky, (0,200),(600,200),5)
    pygame.draw.line(screen,Sky, (0,400),(600,400),5)
    pygame.draw.line(screen,Sky, (200,0),(200,600),5)
    pygame.draw.line(screen,Sky, (400,0),(400,600),5)

def figure():
    for row in range(3):
        for col in range(3):
            if Board[row][col] == 1:
                pygame.draw.circle(screen,(19, 4, 222), (int(col * 200 + 100),int(row * 200 + 100)), 60 , 12)
            elif Board[row][col] == 2:
                pygame.draw.line(screen,(255, 0, 0),(col * 200 + 55, row * 200 + 200 - 55),(col * 200 + 200 - 55, row * 200 + 55),20)
                pygame.draw.line(screen,(255, 0, 0),(col * 200 + 55, row * 200 + 55),(col * 200 + 200 - 55, row * 200 + 200 - 55),20)    

def mark(row,col,player):
    Board[row][col] = player

def avail(row,col):
    return Board[row][col] == 0

def IsFull():
    for row in range(3):
        for col in range(3):
            if Board[row][col] == 0:
                return False
    return True      

def winner(player):

    for col in range(3):
        if Board[0][col] == player and Board[1][col] == player and Board[2][col] == player:
            verticalLine(col,player)
            return True

    for row in range(3):
        if Board[row][0] == player and Board[row][1] == player and Board[row][2] == player:
            horizontalLine(row,player)   
            return True     

    if Board[2][0] == player and Board[1][1] == player and Board[0][2] == player: 
        ascDiagonal(player)    
        return True

    if Board[0][0] == player and Board[1][1] == player and Board[2][2] == player: 
        descDiagonal(player) 
        return True

    return False         


def verticalLine(col, player):
	posX = col * 200 + 100

	if player == 1:
		color = (19, 4, 222)
	elif player == 2:
		color = (255,0,0)

	pygame.draw.line( screen, color, (posX, 15), (posX,600 - 15), 15 )

def horizontalLine(row, player):
	posY = row * 200 + 100

	if player == 1:
		color = (19, 4, 222)
	elif player == 2:
		color = (255,0,0)

	pygame.draw.line( screen, color, (15, posY), (600 - 15, posY), 15 )

def ascDiagonal(player):
	if player == 1:
		color = (19, 4, 222)
	elif player == 2:
		color = (255,0,0)

	pygame.draw.line( screen, color, (15, 600 - 15), (600 - 15, 15), 15 )

def descDiagonal(player):
	if player == 1:
		color = (19, 4, 222)
	elif player == 2:
		color = (255,0,0)

	pygame.draw.line( screen, color, (15, 15), (600 - 15, 600 - 15), 15 )

def restart():
	screen.fill( (0,0,0) )
	draw_lines()
	for row in range(3):
		for col in range(3):
			Board[row][col] = 0    


draw_lines()

player = 1
gameOver = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            MouseX = event.pos[0]
            MouseY = event.pos[1]   

            Clickrow = int(MouseY // square_size)
            ClickCol = int(MouseX // square_size)

            if avail(Clickrow, ClickCol):
                if player == 1:
                    mark(Clickrow,ClickCol,1)
                    if winner(player):
                        gameOver = True
                    player = 2

                elif player == 2:
                    mark(Clickrow,ClickCol,2)
                    if winner(player):
                        gameOver = True
                    player = 1

                figure()    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()        



    pygame.display.update()        