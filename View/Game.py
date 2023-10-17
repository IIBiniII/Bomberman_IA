from View import Player

from tkinter import *

class Game(Frame):
    
    def __init__(self,master):
        super().__init__(master)

        self.player = Player(self,"player 1",w=self.master.winfo_width()-1,h=self.master.winfo_height()-1)
        self.player.pack()
    
