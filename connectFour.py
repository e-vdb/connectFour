#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:02:49 2021

@author: Emeline
"""
import tkinter as tk
import numpy as np
import random

ROW_COUNT = 6
COLUMN_COUNT = 7
WIDTH=50
LENGTH=40
listMessage=['Click on Game to start a new game',
             'Player 1 wins. Click on Game to start a new game',
             'Player 2 wins. Click on Game to start a new game']
onePlayer=True
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

def mode_1HumanPlayer():
    global onePlayer
    onePlayer=True
    game()

def mode_2HumanPlayers():
    global onePlayer
    onePlayer=False
    game()

def game():
    global can,turn,game_over,board,message
    can.delete(tk.ALL)
    board=create_board()
    game_over=False
    turn=0
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            can.create_oval(10+WIDTH*j,10+WIDTH*i,10+LENGTH+WIDTH*j,10+LENGTH+WIDTH*i,outline='white')
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
            can.create_oval(10+col*WIDTH,10+(ROW_COUNT-1)*WIDTH-row*WIDTH,10+LENGTH+col*WIDTH,10+(ROW_COUNT-1)*WIDTH+LENGTH-row*WIDTH,fill=color,outline='white')
            if winner(board,player):
                game_over=True  
                message.configure(text=listMessage[player])
    window.after(500,nextPlayer)

def nextPlayer():
    global turn
    turn+=1
    if onePlayer and turn%2!=0 and not game_over:
        idCol=random.randint(0,6)
        draw(board,idCol)
        
############################################################################
# Help menu
############################################################################  
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
    ruleWindow=tk.Toplevel()
    ruleWindow.title("How to play")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lab_Rule=tk.Label(ruleWindow,text=gameRules,fg="black", anchor="e", justify=tk.LEFT)
    lab_Rule.pack(side=tk.TOP)
    ruleWindow.mainloop()


def about():
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow,text=about,fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.mainloop()  
############################################################################
# Graphics window
############################################################################
window = tk.Tk()
window.title("Connect Four")

############################################################################
# Menus
############################################################################  
top = tk.Menu(window)
window.config(menu=top)
jeu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=jeu)
submenu=tk.Menu(jeu, tearoff=False)
jeu.add_cascade(label='New Game', menu=submenu)
submenu.add_command(label='Versus AI', command=mode_1HumanPlayer)
submenu.add_command(label='2 players', command=mode_2HumanPlayers)
jeu.add_command(label='Exit',command=window.destroy)
helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='How to play?',command=printRules)
helpMenu.add_command(label='About',command=about)

############################################################################
# Other
############################################################################ 
can = tk.Canvas(window,bg='black',height=330,width=360)
can.pack(side=tk.BOTTOM)

message=tk.Label(window, text=listMessage[0])
message.pack(side=tk.TOP)
game_over=True
board=create_board()

buttons=[tk.Button(window,text=i,command=lambda x=i:draw(board,x)) for i in range(COLUMN_COUNT)]
for col in range(COLUMN_COUNT):
    buttons[col].pack(side=tk.LEFT)
for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            can.create_oval(10+WIDTH*j,10+WIDTH*i,10+LENGTH+WIDTH*j,10+LENGTH+WIDTH*i,outline='white')

window.mainloop()