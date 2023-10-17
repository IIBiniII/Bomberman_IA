from View import Player

from tkinter import *

class Game(Frame):
    
    def __init__(self,master):
        super().__init__(master)

        self.player = Player(self,"player 1")
        self.player.pack()#place(x=10,y=10)
    
