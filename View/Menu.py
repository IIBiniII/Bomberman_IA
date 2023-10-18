from tkinter import *
from Controller import ControleurPlayBoutonMenu,ControleurEntrainementIABouton

class Menu(Frame):

    def __init__(self, master):
        super().__init__(master)

        controleurplay = ControleurPlayBoutonMenu(self.master)
        controleurEntrainementIA = ControleurEntrainementIABouton(self.master)

        self.configure(bg="light blue")


        self.boutonPlay = Button(self, text="jouer entre joueur")
        self.boutonPlay.bind("<Button-1>", controleurplay.OnAction)

        self.boutonEntrainement = Button(self, text="Entrainement IA")
        self.boutonEntrainement.bind("<Button-1>", controleurEntrainementIA.OnAction)

        # Utilise grid pour centrer le bouton en X et en Y
        self.boutonPlay.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.boutonEntrainement.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.pack()


