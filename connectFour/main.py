#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:02:49 2021

@author: Emeline
"""

import tkinter as tk
import random
from help_GUI import about, print_rules
from connectFour import create_board, valid_move
from connectFour import find_row, drop_piece, check_winning_move, winner


ROW_COUNT = 6
COLUMN_COUNT = 7
WIDTH = 50
LENGTH = 40
listMessage=['Click on Game to start a new game',
             'Player 1 wins. Click on Game to start a new game',
             'Player 2 wins. Click on Game to start a new game']
difficulty_AI = 1
onePlayer = True


def mode_1HumanPlayer() -> None:
    """
    Lauch game for one human player versus AI.

    Returns
    -------
    None.

    """
    global onePlayer
    onePlayer = True
    game()

def difficulty_easy() -> None:
    """
    Set the AI-difficulty level to easy.

    Returns
    -------
    None.

    """
    global difficulty_AI
    difficulty_AI = 0

def difficulty_intermediate():
    """
    Set the AI-difficulty level to intermediate.

    Returns
    -------
    None.

    """
    global difficulty_AI
    difficulty_AI = 1

def mode_2HumanPlayers() -> None:
    """
    Lauch game for two human players.

    Returns
    -------
    None.

    """
    global onePlayer
    onePlayer = False
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

# Selects random valid column
def random_AI(board):
    valid_moves = [col for col in range(COLUMN_COUNT) if board[ROW_COUNT-1][col] == 0]
    return random.choice(valid_moves)


def smart_AI(board):
    valid_moves = [col for col in range(COLUMN_COUNT) if board[ROW_COUNT-1][col] == 0]
    for col in valid_moves:
        if check_winning_move(board,col,2):
            return col
    for col in valid_moves:
        if check_winning_move(board,col,1):
            return col  
    return random.choice(valid_moves)


def nextPlayer():
    global turn,difficulty_AI
    turn+=1
    if onePlayer and turn%2!=0 and not game_over:
        if difficulty_AI == 0:
            idCol=random_AI(board)
        elif difficulty_AI == 1:
            idCol=smart_AI(board)
        draw(board,idCol)
        

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

settingsMenu = tk.Menu(top,tearoff=False)
top.add_cascade(label='Difficulty', menu=settingsMenu)
settingsMenu.add_command(label='Easy',command=difficulty_easy)
settingsMenu.add_command(label='Intermediate',command=difficulty_intermediate)

helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='How to play?', command=print_rules)
helpMenu.add_command(label='About', command=about)

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
