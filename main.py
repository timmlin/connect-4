import math 
import pygame
from sys import exit
from time import sleep

BOARDWIDTH = 7
BOARDHEIGHT = 6

SQUARESIZE = 75
TOKENSIZE = 30

SCREENWIDTH = SQUARESIZE * BOARDWIDTH 
SCREENHEIGHT = SQUARESIZE * (BOARDHEIGHT + 1)


#------------------------------------------------
#-----------GUI-Functions------------------------
#------------------------------------------------
def drawBoard(screen, nextEmptySpace, board, isPlayerOne):
    """draws the connect 4 board and backgorund black lines are drawn to seperate the spaces
    each square has a white circle to indicate the square is empty or filled with a red or yellow
    token. The current row the mouse is in is highlighted in grey."""
    pygame.draw.rect(screen,(255,255,255), (0,0, SCREENWIDTH, SQUARESIZE)) # draws a white rectangle above the baord to prvent multiple tokens being drawn
    
    #draws the blue board
    pygame.draw.rect(screen, (0,0,225), (0,SQUARESIZE, SCREENWIDTH, SCREENHEIGHT)) 

    #draws horizontal lines on the board
    for rowNum in range(1, BOARDHEIGHT +1):
            pygame.draw.line(screen, (0,0,0), (0, SQUARESIZE * rowNum), (SCREENWIDTH, SQUARESIZE * rowNum), width=3)
    #draws vertical lines on the board
    for colNum in range(BOARDWIDTH+1):
            pygame.draw.line(screen, (0,0,0), (SQUARESIZE * colNum, SQUARESIZE ), (SQUARESIZE * colNum, SCREENHEIGHT), width=3)

    #highlights the current row 
    for colNum in range(BOARDWIDTH+1):
        if nextEmptySpace[0] > SQUARESIZE * colNum and nextEmptySpace[0] <= SQUARESIZE * (colNum + 1):
            pygame.draw.line(screen, (100,100,100), ((SQUARESIZE * (colNum + 1)), SQUARESIZE ), ((SQUARESIZE * (colNum + 1)), SCREENHEIGHT), width=3)                
            pygame.draw.line(screen, (100,100,100), (SQUARESIZE * colNum, SQUARESIZE ), (SQUARESIZE * colNum, SCREENHEIGHT), width=3)

    #draws the tokens or empty spaces on board
    for colNum in range(BOARDWIDTH):
         for rowNum in range(BOARDHEIGHT):
            if board[rowNum][colNum] == 'R':
                pygame.draw.circle(screen, (255,0,0), (SQUARESIZE*colNum + (SQUARESIZE / 2), SQUARESIZE*(rowNum+1)+ SQUARESIZE / 2), TOKENSIZE)
            elif board[rowNum][colNum] == 'Y':
                pygame.draw.circle(screen, (255,255,0), (SQUARESIZE*colNum + (SQUARESIZE / 2), SQUARESIZE*(rowNum+1)+ SQUARESIZE / 2), TOKENSIZE)
            else:
                 pygame.draw.circle(screen, (255,255,255), (SQUARESIZE*colNum + (SQUARESIZE / 2), SQUARESIZE*(rowNum+1)+ SQUARESIZE / 2), TOKENSIZE)
    
    #draws a visual representation of the token the player is about to use"""
    if isPlayerOne:
        pygame.draw.circle(screen, (255,0,0), (nextEmptySpace[0], SQUARESIZE / 2), TOKENSIZE)
    else:
        pygame.draw.circle(screen, (255,255,0), (nextEmptySpace[0], SQUARESIZE / 2), TOKENSIZE)

     


def playerWin(isPlayerOne, screen):

    #creats the win message and draws it to the screen
    winTextfont = pygame.font.Font('freesansbold.ttf', 64)
    if isPlayerOne:
        winText = winTextfont.render('Player One Wins', True, (255,0,0), (0,0,0))
    else:
        winText = winTextfont.render('Player Two Wins', True, (255,255,0), (0,0,0))
    winTextRect = winText.get_rect()
    winTextRect.center = (SCREENWIDTH / 2, SQUARESIZE / 2)
    screen.blit(winText, winTextRect)

    #creates the play again button 
    buttonTextFont = pygame.font.Font('freesansbold.ttf', 24)
    playAgainButtonPos = ((SCREENWIDTH / 2) - 175, (SCREENHEIGHT / 2) - 37)
    playAgainButton = pygame.Surface((150,50))
    playAgainButton.fill((50,50,50))
    playAgainButtonText = buttonTextFont.render('Play Again', True, (225,225,225), (50,50,50))
    playAgainButton.blit(playAgainButtonText, (5,10))

    #creates the quit button
    quitButtonPos = ((SCREENWIDTH / 2) + 25, (SCREENHEIGHT / 2) - 37)
    quitButton = pygame.Surface((150,50))
    quitButton.fill((50,50,50))
    quitButtonText = buttonTextFont.render('Quit', True, (225,225,225), (50,50,50))
    quitButton.blit(quitButtonText, (50,10))

    pygame.display.update()

    sleep(1.5)
    screen.blit(playAgainButton, playAgainButtonPos)
    screen.blit(quitButton, quitButtonPos)

    while True:
        pygame.display.update()

        for event in pygame.event.get():
            #close game window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if playAgainButton.get_rect(topleft=playAgainButtonPos).collidepoint(pos):
                    main()
                elif quitButton.get_rect(topleft=quitButtonPos).collidepoint(pos):
                    pygame.quit()
                    exit()
    
    
#------------------------------------------
#-------Game-Logic-Functions---------------
#------------------------------------------


def initBoard():
    """initialises a 7x6 board of '-'s"""  
    return [[ '-' for j in range(BOARDWIDTH)] for i in range(BOARDHEIGHT)]


def getNextEmptySpace(board, mousePos):
    """retuns the board coordinates of the next empty
    space in the column the mouse is in. Returns None if the column is full"""
    curCol = math.floor(mousePos[0]/SQUARESIZE)
    nextEmptySpace = None

    for rowNum in range(BOARDHEIGHT):
        if board[rowNum][curCol] == '-':
            nextEmptySpace = [rowNum, curCol]
        else:
            break
    return nextEmptySpace

def dropToken(board, nextEmptySpace, isPlayerOne):
    """drops a token in the selected column and returns the new board"""
    if isPlayerOne:
        board[nextEmptySpace[0]][nextEmptySpace[1]] = 'R'
    else:
        board[nextEmptySpace[0]][nextEmptySpace[1]] = 'Y'
    return board


def checkForWin(board, token):
    # Check for a horizontal win
    for row in board:
        for col in range(len(row) - 3):
            if row[col] == row[col + 1] == row[col + 2] == row[col + 3] == token:
                return True

    # Check for a vertical win
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == token:
                return True

    # Check for a diagonal win (from bottom-left to top-right)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == token:
                return True

    # Check for a diagonal win (from top-left to bottom-right)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == token:
                return True

    return False


#----------------------
#---------Main---------
#----------------------

def printBoard(board):
    """draws the board to the terminal"""
    for row in board:
        print(row)
    print("\n")


#main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Connect Four")
    isPlayerOne = True
    board = initBoard()
    turnNum = 0


    while(True):
        mousePos = pygame.mouse.get_pos()
        pygame.display.update()

        for event in pygame.event.get():
            #close game window
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                nextEmptySpace = getNextEmptySpace(board, mousePos)

                if nextEmptySpace != None:
                    board = dropToken(board, nextEmptySpace, isPlayerOne)
                    turnNum += 1
                   
                    printBoard(board)
                    drawBoard(screen, mousePos, board, isPlayerOne) # redraws the board a token has been dropped

                    if turnNum >= 7: #minimum number of turns before win
                        if isPlayerOne:
                            if checkForWin(board, 'R'): #check for player one win 
                                playerWin(isPlayerOne, screen)
                                
                        else:
                            if checkForWin(board, 'Y'): #check for player two win
                                playerWin(isPlayerOne, screen)
                                
                    
                    isPlayerOne = not isPlayerOne

            drawBoard(screen, mousePos, board, isPlayerOne) # redraws the board after each mouse movement


            

if __name__ == "__main__":

    main()