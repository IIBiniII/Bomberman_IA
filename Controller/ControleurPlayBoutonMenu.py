from View import GameView
from Model import BomberManModel

from Controller import *
from View.CopyGameView import GameViewCopy

class ControleurPlayBoutonMenu(MainControleur):

    

    def __init__(self,View) -> None:
        self.view = View

    def OnAction(self,event):

        if not MainControleur.Model.gameRuning:
            self.view.game = GameViewCopy()#GameView()
            MainControleur.Model.gameRuning = True
        else:
            print("une partie est déja lancer")