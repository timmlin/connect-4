
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
            self.assertEqual(getNextEmptySpace(board, [125*colNum, 125]), [BOARDHEIGHT-1, colNum])


    def testNonEmptyBoard(self):
        """ tests the token will be dropped to the next empty space
        when the column is not empty"""
        board = initBoard()
        board[3][3] = 'Y'
        self.assertEqual(getNextEmptySpace(board, [3*125, 125]), [2, 3])


    def testFullBoard(self):
        """ tests the token will not be dropped when the column is full"""
        board = initBoard()
        for row in range(BOARDHEIGHT):
            for col in range(BOARDWIDTH):
                board[row][col] = 'R'
        self.assertEqual(getNextEmptySpace(board, [3*125, 125]), None)









if __name__ == '__main__':
    unittest.main()
