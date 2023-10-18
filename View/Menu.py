from tkinter import *
from Controller import ControleurPlayBoutonMenu

class Menu(Frame):

    def __init__(self, master):
        super().__init__(master)

        controleurplay = ControleurPlayBoutonMenu(self.master)

        self.configure(bg="light blue")


        self.boutonPlay = Button(self, text="Play")
        self.boutonPlay.bind("<Button-1>", controleurplay.onAction)

        # Utilise grid pour centrer le bouton en X et en Y
        self.boutonPlay.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.pack()


