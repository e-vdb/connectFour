#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define class game"""

import numpy as np
import tkinter as tk
from connectFour import find_row, drop_piece, winner, valid_move
from strategyAI import smart_AI, random_AI

ROW_COUNT = 6
COLUMN_COUNT = 7
WIDTH = 50
LENGTH = 40
listMessage=['Click on Game to start a new game',
             'Player 1 wins. Click on Game to start a new game',
             'Player 2 wins. Click on Game to start a new game']

class Game:
    
    def __init__(self, can, lab_message, window):
        self.onePlayer = True
        self.difficulty_AI = 1
        self.can = can
        self.window = window
        self.lab_message = lab_message
        self.create_board()
        self.turn = 0
        self.game_over = False
        self.draw_board()

    def create_board(self) -> None:
        """
        Create a board.
    
        Returns
        -------
        board : np.array
            Array that stores the board of the connect Four game.
    
        """
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    
    def draw_board(self):
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.can.create_oval(10+WIDTH*j,
                                     10+WIDTH*i,
                                     10+LENGTH+WIDTH*j,
                                     10+LENGTH+WIDTH*i,
                                     outline='white')
        self.lab_message.configure(text='player 1')
    
    def reinit(self):
        self.can.delete(tk.ALL)
        self.create_board()
        self.turn = 0
        self.game_over = False
        self.draw_board()

    def play(self, col):
        if not self.game_over:
            if self.turn %2 == 0:
                color = 'red'
                player = 1
                self.lab_message.configure(text='player 2')
            else:
                color = 'yellow'
                player = 2
                self.lab_message.configure(text='player 1')
            if valid_move(self.board, col):
                row = find_row(self.board, col)
                drop_piece(self.board, row, col, player)
                self.can.create_oval(10+col*WIDTH,
                                     10+(ROW_COUNT-1)*WIDTH-row*WIDTH,
                                     10+LENGTH+col*WIDTH,
                                     10+(ROW_COUNT-1)*WIDTH+LENGTH-row*WIDTH,
                                     fill=color, 
                                     outline='white')
                if winner(self.board, player):
                    self.game_over = True  
                    self.lab_message.configure(text=listMessage[player])
        self.window.after(500, self.nextPlayer)

    
    def mode_1HumanPlayer(self) -> None:
        """
        Lauch game for one human player versus AI.
    
        Returns
        -------
        None.
    
        """
        self.onePlayer = True
        self.reinit()

    def difficulty_easy(self) -> None:
        """
        Set the AI-difficulty level to easy.
    
        Returns
        -------
        None.
    
        """
        self.difficulty_AI = 0

    def difficulty_intermediate(self):
        """
        Set the AI-difficulty level to intermediate.
    
        Returns
        -------
        None.
    
        """
        self.difficulty_AI = 1
    
    def mode_2HumanPlayers(self) -> None:
        """
        Lauch game for two human players.
    
        Returns
        -------
        None.
    
        """
        self.onePlayer = False
        self.reinit()

    def nextPlayer(self) -> None:
        """
        Increment the turn to switch players.
        
        Returns
        -------
        None.
    
        """
        self.turn += 1
        # In versus AI mode only
        if self.onePlayer and self.turn%2 !=0 and not self.game_over:
            if self.difficulty_AI == 0:
                idCol = random_AI(self.board)
            elif self.difficulty_AI == 1:
                idCol = smart_AI(self.board)
            self.play(idCol)