from tkinter import *

class Game(Frame):
    
    def __init__(self,master):
        super().__init__(master)

        player = Label(self,text="player 1")
        player.pack()#place(x=10,y=10)