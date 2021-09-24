# Connect Four

## Summary

Connect four game for two human players or one human player against AI player.

Code written in python3 with graphics user interface (GUI) using Tkinter.

## Connect Four

Connect four is a two-players game.

To learn more about this game, visit https://en.wikipedia.org/wiki/Connect_Four

## Repository content

To play the game, save the following files in the same directory.

* connectFour.py : Python 3 script
* rules_eng.txt : plain text document that contains the rules of the game
* about.txt : plain text document that contains copyright and license information

## Tkinter interface

### Interface

Board 7 x 6.
Buttons (from 0 to 6) to select the column.

![gui](https://user-images.githubusercontent.com/82372483/134669717-dd738288-efd9-4c5e-bcd4-33277eabeae5.png)

### Help

From the GUI you can read How to play? as well as copyright and license information.

### Example of game

![game](https://user-images.githubusercontent.com/82372483/134669778-8fd9c399-0322-426f-977a-08ee00de85c4.png)

### Game mode

From the menu you can start a new game. Two modes are available.

#### One human player
Play against AI. You can change the difficulty level thanks to *Difficulty* menu.

* Easy : The AI chooses randomly a column among allowed moves
* Intermediate : The AI chooses a column among allowed moves following
   *  valid move that makes AI win
   *  valid move that makes human win
   *  random move

#### Two human players
Play with a friend.

