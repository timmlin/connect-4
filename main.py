import pygame
from sys import exit

BOARDWIDTH = 7
BOARDHEIGHT = 6

SCREENWIDTH = 125 * BOARDWIDTH 
SCREENHEIGHT = 125 * (BOARDHEIGHT + 1)


def initBoard():
    """initialises a 7x6 board of -s"""
    return [[ '-' for j in range(BOARDWIDTH)] for i in range(BOARDHEIGHT)]

def drawBoard(screen, mousePos, board ):
    """draws the connect 4 board and backgorund"""
    pygame.draw.rect(screen,(255,255,255), (0,0, SCREENWIDTH, 125)) # draws a white rectangle above the baord to prvent multiple tokens being drawn
    pygame.draw.rect(screen, (0,0,225), (0,125, SCREENWIDTH, SCREENHEIGHT)) 

    #draws horizontal lines
    for rowNum in range(1, BOARDHEIGHT +1):
            pygame.draw.line(screen, (0,0,0), (0, 125 * rowNum), (SCREENWIDTH, 125 * rowNum), width=3)
    #draws vertical lines
    for colNum in range(BOARDWIDTH+1):
            pygame.draw.line(screen, (0,0,0), (125 * colNum, 125 ), (125 * colNum, SCREENHEIGHT), width=3)

    #highlights the current row 
    for colNum in range(BOARDWIDTH+1):
        if mousePos[0] > 125 * colNum and mousePos[0] <= 125 * (colNum + 1):
            pygame.draw.line(screen, (100,100,100), ((125 * (colNum + 1)), 125 ), ((125 * (colNum + 1)), SCREENHEIGHT), width=3)                
            pygame.draw.line(screen, (100,100,100), (125 * colNum, 125 ), (125 * colNum, SCREENHEIGHT), width=3)

    #draws the tokens or empty spaces on board
    for colNum in range(BOARDWIDTH):
         for rowNum in range(BOARDHEIGHT +1 ):
            pygame.draw.circle(screen, (255,255,255), (125*colNum + 62.5, 125*rowNum + 62.5), 50)

     
        

def drawToken(screen, turnOne, mousePos):
    """draws a visual representation of the token the player is about to use"""
    if turnOne:
        pygame.draw.circle(screen, (255,0,0), (mousePos[0], 66), 50)
    else:
        pygame.draw.circle(screen, (255,255,0), (mousePos[0], 66), 50)
     

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("Connect Four")
    turnOne = True
    board = initBoard()


    while(True):
        mousePos = pygame.mouse.get_pos()
        pygame.display.update()

        for event in pygame.event.get():
            #close game window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEMOTION:
                drawBoard(screen, mousePos, board) # redraws the board after each mouse movement
                drawToken(screen, turnOne, mousePos)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                turnOne = not turnOne
                drawToken(screen, turnOne, mousePos)

        
                







           
                

if __name__ == "__main__":

    main()