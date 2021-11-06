"""
AI player functions.
"""
from connectFour import check_winning_move
import random


ROW_COUNT = 6
COLUMN_COUNT = 7

def random_AI(board) -> int:
    """
    Return the index of the column randomly chosen by the AI.

    Parameters
    ----------
    board : np.array
        Array that stores the board of the connect Four game.

    Returns
    -------
    int
        Column chosen by the AI.

    """
    # Selects random valid column
    valid_moves = [col for col in range(COLUMN_COUNT) if board[ROW_COUNT-1][col] == 0]
    return random.choice(valid_moves)


def smart_AI(board) -> int:
    """
    Return the index of the column chosen by the AI.

    Parameters
    ----------
    board : np.array
        Array that stores the board of the connect Four game.

    Returns
    -------
    int
        Column chosen by the AI.

    """
    valid_moves = [col for col in range(COLUMN_COUNT) if board[ROW_COUNT-1][col] == 0]
    # Checks whether AI can win
    for col in valid_moves:
        if check_winning_move(board,col,2):
            return col
    # Checks whether humab player can win
    for col in valid_moves:
        if check_winning_move(board,col,1):
            return col  
    # Selects random valid column
    return random.choice(valid_moves)