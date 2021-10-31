"""
Connect four game functions.
"""
import numpy as np


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board() -> None:
    """
    Create a board.

    Returns
    -------
    board : np.array
        Array that stores the board of the connect Four game.

    """
    board=np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def valid_move(board, col) -> bool :
    """
    Check whether the column chosen by the player is free?

    Parameters
    ----------
    board : TYPE
        DESCRIPTION.
    col : TYPE
        DESCRIPTION.

    Returns
    -------
    boolean
        DESCRIPTION.

    """
    return board[ROW_COUNT-1][col] == 0

def find_row(board, col) -> int:
    """
    Return the row number that can be played for a given column.

    Parameters
    ----------
    board : np.array
        Connect four board.
    col : int64
        Column number chosen by the player.

    Returns
    -------
    int
        Row number that can be played.

    """
    for row in range(ROW_COUNT):
        if board[row][col]==0:
            return row

def drop_piece(board, row, col, piece) -> None:
    """
    Change the current state of the board.

    Parameters
    ----------
    board : np.array
        Board of the connect four game.
    row : int64
        Row number in the board (included between 0 and ROW_COUNT).
    col : int64
        Column number in the board (included between 0 and COLUMN_COUNT).
    piece : int64
        Number to represent the player (1 or 2).

    Returns
    -------
    None.

    """
    board[row][col] = piece  

def check_winning_move(board,col,player):
    row = find_row(board, col)
    next_grid=board.copy()
    drop_piece(next_grid,row,col,player)
    if(winner(next_grid,player)):
        return True
    else:
        return False

def winner(board,player):
    # check for 4 in horizontal direction
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT-3):
            if (board[row][col]==player) and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player :
                return True
    # check for 4 in vertical direction
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-3):
            if board[row][col]==player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player :
                return True
    # check for 4 in diagonal direction
    for row in range(ROW_COUNT-3):
        for col in range(COLUMN_COUNT-3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player :
                return True
    # check for 4 in diagonal direction (opposite)
    for row in range(3,ROW_COUNT):
        for col in range(COLUMN_COUNT-3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player :
                return True
    return False