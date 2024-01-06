import math 
import pygame
from sys import exit

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
    pygame.draw.rect(screen, (0,0,225), (0,SQUARESIZE, SCREENWIDTH, SCREENHEIGHT)) 

    #draws horizontal lines
    for rowNum in range(1, BOARDHEIGHT +1):
            pygame.draw.line(screen, (0,0,0), (0, SQUARESIZE * rowNum), (SCREENWIDTH, SQUARESIZE * rowNum), width=3)
    #draws vertical lines
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
                   
                    if turnNum >= 7: #minimum number of turns before win
                        if isPlayerOne:
                            if checkForWin(board, 'R'): #check for player one win 
                                #playerWin(isPlayerOne)
                                pass
                        else:
                            if checkForWin(board, 'Y'): #check for player two win
                                #playerWin(isPlayerOne)
                                pass
                    
                    isPlayerOne = not isPlayerOne
                    printBoard(board)

            drawBoard(screen, mousePos, board, isPlayerOne) # redraws the board after each mouse movement


            

if __name__ == "__main__":

    main()