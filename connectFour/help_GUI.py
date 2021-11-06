"""
Define functions for the Menu Help.

@author: Emeline
"""
import tkinter as tk


def print_rules() -> None:
    """
    Load a text files 'rules_eng.txt' saved inside the same directory.
    Open a second window.

    Returns
    -------
    None.

    """
    ruleWindow=tk.Toplevel()
    ruleWindow.title("How to play?")
    with open('rules_eng.txt') as f:
        gameRules=f.read()
    lbl_rules=tk.Label(ruleWindow, text=gameRules, 
                       fg="black", anchor="e", justify=tk.LEFT)
    lbl_rules.pack(side=tk.TOP)
    ruleWindow.resizable(0,0)
    ruleWindow.mainloop()

def about() -> None:
    """
    Load the text document 'about.txt'.
    Open a secondary window.
    Write the content of the text document.

    Returns
    -------
    None.

    """
    aboutWindow=tk.Toplevel()
    aboutWindow.title("About") 
    with open('about.txt') as f:
        about=f.read()
    lbl_about=tk.Label(aboutWindow, text=about, 
                       fg="black", anchor="e", justify=tk.LEFT)
    lbl_about.pack(side=tk.TOP)
    aboutWindow.resizable(0,0)
    aboutWindow.mainloop()