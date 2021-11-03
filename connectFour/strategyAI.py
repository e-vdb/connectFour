"""
AI player functions.
"""
from connectFour import check_winning_move
import random


ROW_COUNT = 6
COLUMN_COUNT = 7

def random_AI(board) -> int:
    # Selects random valid column
    valid_moves = [col for col in range(COLUMN_COUNT) if board[ROW_COUNT-1][col] == 0]
    return random.choice(valid_moves)


def smart_AI(board) -> int:
    valid_moves = [col for col in range(COLUMN_COUNT) if board[ROW_COUNT-1][col] == 0]
    for col in valid_moves:
        if check_winning_move(board,col,2):
            return col
    for col in valid_moves:
        if check_winning_move(board,col,1):
            return col  
    return random.choice(valid_moves)