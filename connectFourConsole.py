#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:02:49 2021

@author: Emeline

Puissance 4 : version console
"""

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board=np.zeros((6,7))
    return board

def valid_move(board,col):
    return board[5][col] == 0

def find_row(board,col):
    for row in range(ROW_COUNT):
        if board[row][col]==0:
            return row

def drop_piece(board,row,col,piece):
    board[row][col]= piece

def play(board,player):
    print("Player {}, Choose a column (0-6)".format(player))
    col = int(input())
    if valid_move(board,col):
            row = find_row(board, col)
            drop_piece(board,row,col,player)

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

def show_board(board):
    print(np.flip(board,0))

# initialisation of game board
board=create_board()
game_over=False
turn=0
while not game_over:
    if turn%2 == 0:
        play(board,1)
        if winner(board,1):
            game_over=True
            print("Player 1 wins")
    else :
        play(board,2)
        if winner(board,2):
            game_over=True
            print("Player 2 wins")
    show_board(board)
    turn+=1

