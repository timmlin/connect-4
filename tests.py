
import unittest

from main import *


class testInitBoard(unittest.TestCase):
    """tests that the board is initialized correctly.
        the board should always be initialised as a 2d array
        of '-'s with a height of BOARDHEIGHT and a width of BOARDWIDTH
    """
    def testInitBoard(self):
        board = initBoard()
        self.assertEqual(len(board), BOARDHEIGHT)
        self.assertEqual(len(board[0]), BOARDWIDTH)
        for row in board:
            for cell in row:
                self.assertEqual(cell, '-')
        

class testGetNextEmptySpace(unittest.TestCase):
    """tests the GetNextEmptySpace function is able 
    to find the next empty space in the column"""

    def testEmptyBoard(self):
        """ tests the token will be dropped to the bottom row when
        the column is empty"""
        board = initBoard()
        
        for colNum in range(BOARDWIDTH):
            self.assertEqual(getNextEmptySpace(board, [SQUARESIZE*colNum, SQUARESIZE]), [BOARDHEIGHT-1, colNum])


    def testNonEmptyBoard(self):
        """ tests the token will be dropped to the next empty space
        when the column is not empty"""
        board = initBoard()
        board[3][3] = 'Y'
        self.assertEqual(getNextEmptySpace(board, [3*SQUARESIZE, SQUARESIZE]), [2, 3])


    def testFullBoard(self):
        """ tests the token will not be dropped when the column is full"""
        board = initBoard()
        for row in range(BOARDHEIGHT):
            for col in range(BOARDWIDTH):
                board[row][col] = 'R'
        self.assertEqual(getNextEmptySpace(board, [3*SQUARESIZE, SQUARESIZE]), None)



class testDropToken(unittest.TestCase):
    """tests the dropToken function will place a token in the
    correct column and the correct colour is dropped"""

    def testDropPlayerOneToken(self):
        """drops player ones's red token in column 3"""
        board = initBoard()
        board = dropToken(board, [3, 0], True)
        self.assertEqual(board[3][0], 'R')

    def testDropPlayerTwoToken(self):
        """drops player two's yellow token in column 5"""
        board = initBoard()
        board = dropToken(board, [5,6], False)
        self.assertEqual(board[5][6], 'Y')




class testCheckForWin(unittest.TestCase):
    """tests the check for a win condition function"""

#----------horizontal-tests------------
    def testHorizontalWin(self):
        board = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'R', 'R', 'R', 'R', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertTrue(checkForWin(board, 'R'))

    def testWrappedHorizontalWin(self):
        """checks the win check returns false when 
        the tokens wrap around the board"""
        board = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['Y', '-', '-', '-', 'Y', 'Y', 'Y'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertFalse(checkForWin(board, 'Y'))

    def testHorizontalThreeInARow(self):
        """checks the win check returns false when 
        there are only 3 in a row"""
        board = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', 'R', 'R', 'R', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertFalse(checkForWin(board, 'R'))



#----------vertical-tests------------
    def testVerticalWin(self):
        board = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'Y', '-', '-', '-', '-'],
            ['-', '-', 'Y', '-', '-', '-', '-'],
            ['-', '-', 'Y', '-', '-', '-', '-'],
            ['-', '-', 'Y', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertTrue(checkForWin(board, 'Y'))

    def testWrappedVerticalWin(self):
        board = [
            ['-', '-', '-', '-', '-', 'R', '-'],
            ['-', '-', '-', '-', '-', 'R', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', 'R', '-'],
            ['-', '-', '-', '-', '-', 'R', '-']
        ]
        self.assertFalse(checkForWin(board, 'R'))


    def testVerticalThreeInARow(self):
        board = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', 'R', '-', '-', '-'],
            ['-', '-', '-', 'R', '-', '-', '-'],
            ['-', '-', '-', 'R', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertFalse(checkForWin(board, 'R'))


#----------Diagonal-tests------------
    def testDiagonalWin(self):
        board = [
            ['-', '-', '-', 'R', '-', '-', '-'],
            ['-', '-', '-', '-', 'R', '-', '-'],
            ['-', '-', '-', '-', '-', 'R', '-'],
            ['-', '-', '-', '-', '-', '-', 'R'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertTrue(checkForWin(board, 'R'))

    def testWrappedDiagonalWin(self):
        board = [
            ['-', '-', '-', '-', 'Y', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', 'Y', '-', '-', '-', '-', '-'],
            ['-', '-', 'Y', '-', '-', '-', '-'],
            ['-', '-', '-', 'Y', '-', '-', '-']
        ]
        self.assertFalse(checkForWin(board, 'Y'))

    def testNegativeDiagonalWin(self):
        board = [
            ['-', '-', '-', '-', 'R', '-', '-'],
            ['-', '-', '-', 'R', '-', '-', '-'],
            ['-', '-', 'R', '-', '-', '-', '-'],
            ['-', 'R', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertTrue(checkForWin(board, 'R'))

    def testWrappedNegativeDiagonalWin(self):
        board = [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', 'R', '-', '-', '-', '-', '-'],
            ['R', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', 'R'],
            ['-', '-', '-', '-', '-', 'R', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]
        self.assertFalse(checkForWin(board, 'R'))


if __name__ == '__main__':
    unittest.main()
