from tkinter import *


class TrainView(Frame):


    def __init__(self,master,nbGen) -> None:
        
        super().__init__(master)
        textGen = Label(self,text = f"Génération Numéro : {nbGen}")

        boutonNextGen = Button(self,text="Génération suivante")


        textGen.pack()
        boutonNextGen.pack()
        