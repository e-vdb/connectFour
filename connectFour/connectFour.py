"""
Connect four game functions.
"""
import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    """
    Create a board.

    Returns
    -------
    board : np.array
        Array that stores the board of the connect Four game.

    """
    board=np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def valid_move(board, col):
    return board[ROW_COUNT-1][col] == 0