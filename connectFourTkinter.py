#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:02:49 2021

@author: Emeline
"""
import tkinter as tk
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
    

def play(board,player,color):
    print("Player {}, Choose a column (0-6)".format(player))
    col = int(input())
    if valid_move(board,col):
            row = find_row(board, col)
            drop_piece(board,row,col,player)
            can.create_oval(100+col*30,250-row*30,120+col*30,270-row*30,fill=color,outline='white')
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


def game():
    global can,turn,game_over,board,message
    can.delete(tk.ALL)
    board=create_board()
    game_over=False
    turn=0
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            can.create_oval(100+30*j,100+30*i,120+30*j,120+30*i,outline='white')
    message.configure(text='player 1')
        

def draw(board,col):
    global turn,game_over,message
    if not game_over:
        if turn%2 == 0:
            color='red'
            player=1
            message.configure(text='player 2')
        else:
            color='yellow'
            player=2
            message.configure(text='player 1')
        if valid_move(board,col):
            row = find_row(board, col)
            drop_piece(board,row,col,player)
            can.create_oval(100+col*30,250-row*30,120+col*30,270-row*30,fill=color,outline='white')
            if winner(board,player):
                game_over=True  
                print("Winner")
               
        turn+=1

############################################################################
# Graphics window
############################################################################
window = tk.Tk()
window.title("Connect Four")


top = tk.Menu(window)
window.config(menu=top)
jeu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=jeu)
jeu.add_command(label='New game',command=game)
jeu.add_command(label='Exit',command=window.destroy)

can = tk.Canvas(window,bg='black',height=500,width=500)
can.pack(side=tk.BOTTOM)

message=tk.Label(window, text='Begin a new game')
message.pack(side=tk.TOP)
game()

buttons=[tk.Button(window,text=i,command=lambda x=i:draw(board,x)) for i in range(COLUMN_COUNT)]
for col in range(COLUMN_COUNT):
    buttons[col].pack(side=tk.LEFT)




window.mainloop()