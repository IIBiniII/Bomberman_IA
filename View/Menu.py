from tkinter import *
from Controler import ControleurPlayBoutonMenu

class Menu(Frame):

    def __init__(self,master):

        super().__init__(master)

        controleurplay = ControleurPlayBoutonMenu(self.master)

        self.boutonPlay = Button(self,text="play")
        self.boutonPlay.bind("<Button-1>",controleurplay.onAction)

        self.boutonPlay.grid(row=0,column=0)