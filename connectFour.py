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
WIDTH=50
LENGTH=40
listMessage=['Begin a new game','Player 1 wins','Player 2 wins']

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
            can.create_oval(100+WIDTH*j,100+WIDTH*i,100+LENGTH+WIDTH*j,100+LENGTH+WIDTH*i,outline='white')
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
            can.create_oval(100+col*WIDTH,100+(ROW_COUNT-1)*WIDTH-row*WIDTH,100+LENGTH+col*WIDTH,100+(ROW_COUNT-1)*WIDTH+LENGTH-row*WIDTH,fill=color,outline='white')
            if winner(board,player):
                game_over=True  
                message.configure(text=listMessage[player])
        turn+=1

def printRules():
    '''
    Function used inside GUI to generate a window that displays the rules of the game 
    
    Loads a text files 'rules_eng.txt' saved inside the same directory.
    Opens a second window.
    Writes the content of the text document 
    
    Returns
    -------
    None.

    '''
    global ruleWindow
    ruleWindow=tk.Tk()
    ruleWindow.title("Connect four: rules")
    frameRule=tk.Canvas(ruleWindow,bg='white',height=500,width=500)
    frameRule.pack()  
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lab_Rule=tk.Label(frameRule,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lab_Rule.pack(side=tk.TOP)
    ruleWindow.mainloop()


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
top.add_command(label='Rules',command=printRules)

can = tk.Canvas(window,bg='black',height=500,width=500)
can.pack(side=tk.BOTTOM)

message=tk.Label(window, text=listMessage[0])
message.pack(side=tk.TOP)
game_over=True
board=create_board()

buttons=[tk.Button(window,text=i,command=lambda x=i:draw(board,x)) for i in range(COLUMN_COUNT)]
for col in range(COLUMN_COUNT):
    buttons[col].pack(side=tk.LEFT)

window.mainloop()