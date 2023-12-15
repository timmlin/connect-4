
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
        
