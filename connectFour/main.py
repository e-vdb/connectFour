#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI"""

import tkinter as tk
from help_GUI import about, print_rules
from game_class import Game


ROW_COUNT = 6
COLUMN_COUNT = 7
WIDTH = 50
LENGTH = 40
listMessage=['Click on Game to start a new game',
             'Player 1 wins. Click on Game to start a new game',
             'Player 2 wins. Click on Game to start a new game']

        
############################################################################
# Graphics window
############################################################################
window = tk.Tk()
window.title("Connect Four")
can = tk.Canvas(window,bg='black', height=330, width=360)
can.pack(side=tk.BOTTOM)
message=tk.Label(window)
message.pack(side=tk.TOP)
game = Game(can, message, window)
############################################################################
# Menus
############################################################################  
top = tk.Menu(window)
window.config(menu=top)
jeu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Game', menu=jeu)
submenu=tk.Menu(jeu, tearoff=False)
jeu.add_cascade(label='New Game', menu=submenu)
submenu.add_command(label='Versus AI', command=game.mode_1HumanPlayer)
submenu.add_command(label='2 players', command=game.mode_2HumanPlayers)
jeu.add_command(label='Exit',command=window.destroy)

settingsMenu = tk.Menu(top,tearoff=False)
top.add_cascade(label='Difficulty', menu=settingsMenu)
settingsMenu.add_command(label='Easy', command=game.difficulty_easy)
settingsMenu.add_command(label='Intermediate', command=game.difficulty_intermediate)

helpMenu = tk.Menu(top, tearoff=False)
top.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='How to play?', command=print_rules)
helpMenu.add_command(label='About', command=about)

############################################################################
# Buttons
############################################################################ 
buttons=[tk.Button(window,text=i,command=lambda x=i: game.play(x)) for i in range(COLUMN_COUNT)]
for col in range(COLUMN_COUNT):
    buttons[col].pack(side=tk.LEFT)

window.mainloop()
