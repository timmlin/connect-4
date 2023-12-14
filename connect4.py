import pygame
from sys import exit

BOARDWIDTH = 7
BOARDHEIGHT = 6

SCREENWIDTH = 125 * BOARDWIDTH 
SCREENHEIGHT = 125 * (BOARDHEIGHT + 1)


def initBoard():
    # creates a 7x6 board of 0s
    return [[ 0 for j in range(7)] for i in range(6)]

def drawBoard(screen):
        pygame.draw.rect(screen,(255,255,255), (0,0, SCREENWIDTH, 125)) # draws a white rectangle above the baord to prvent multiple tokens
        pygame.draw.rect(screen, (0,0,225), (0,125, SCREENWIDTH, SCREENHEIGHT)) 

        for row in range(1, SCREENHEIGHT):
             pygame.draw.line(screen, (0,0,0), (0, 125 * row), (SCREENWIDTH, 125 * row), width=3)

        for column in range(1, SCREENWIDTH):
             pygame.draw.line(screen, (0,0,0), (125 * column, 125 ), (125 * column, SCREENHEIGHT), width=3)
        


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("Connect Four")

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
                drawBoard(screen) # redraws the board after each mouse movement
                pygame.draw.circle(screen, (255,0,0), (mousePos[0], 66), 50)

        
                







           
                

if __name__ == "__main__":

    main()