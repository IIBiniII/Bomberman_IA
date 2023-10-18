from tkinter import *
import View
from View import GameView

class OptionView(Tk):


    def __init__(self) -> None:
        
        super().__init__()
        self.geometry("500x500")
        self.runing = True
        self.game : GameView = None
        self.protocol("WM_DELETE_WINDOW", self.stop)

        self.page = View.Menu(self)
        self.configure(bg="light blue")

        self.history = [self.page]

        self.page.pack()

    def goBack(self):
        self.page.forget()
        self.page = self.history[-1]
        del self.history[-1]
        self.page.pack()

    def goTo(self,pannel : Frame):
        self.page.forget()
        self.history.append(self.page)
        self.page = pannel
        self.page.pack()

    def stop(self):
        self.runing = False
    
    def start(self):
        while self.runing:
            if self.game != None:
                if not self.game.update() : #Effectue l'update + vérifie si on a quitté la page
                    self.game.stop()
                    #TODO Afficher sur l'optionView que la partie s'est arrêté 
            self.update()
